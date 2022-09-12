from django.core.management.base import BaseCommand, CommandError
from django.db.models import Q
from django.core.exceptions import MultipleObjectsReturned
from django.contrib.auth import get_user_model

from mighty.functions import get_model, request_kept
from mighty.apps import MightyConfig as conf
from mighty.applications.logger import EnableLogger
from mighty.readers import ReaderXLS
import datetime, sys, csv, os.path

class BaseCommand(BaseCommand, EnableLogger):
    total = 0
    help = 'Command Base override by Mighty'
    position = 0
    prefix_bar = 'Percent'
    current_info = ''
    errors = []
    in_test = False
    loader = False
    userlog_cache = None

    @property
    def user_model(self):
        return get_user_model()

    def get_user(self, info, forlog=False):
        try: 
            return self.user_model.objects.get()
        except self.user_model.DoesNotExist:
            return self.user_model.objects.filter(is_superuser=True).first() if forlog else None

    def get_total(self):
        return self.total if self.total else 0
    
    def set_position(self, pos=1):
        self.position+=pos

    def get_current_info(self):
        return self.current_info

    def progress_bar(self, bar_length=20):
        if self.verbosity > 0 and self.total:
            percent = self.position / self.get_total()
            if self.progressbar:
                arrow = '-' * int(round(percent * bar_length)-1) + '>'
                spaces = ' ' * (bar_length - len(arrow))
                sys.stdout.write("\r{0}: [{1}] {2}% ({3}/{4}) {5}".format(
                    self.prefix_bar,
                    arrow + spaces,
                    int(round(percent * 100)),
                    self.position,
                    self.get_total(),
                    self.get_current_info(),
                    )
                )
                sys.stdout.flush()
            else:
                sys.stdout.write("\r{0}: {1}% ({2}/{3}) {4}".format(
                    self.prefix_bar,
                    int(round(percent * 100)),
                    self.position,
                    self.get_total(),
                    self.get_current_info())
                )
                print()
            if self.position == self.get_total(): print()

    def create_parser(self, prog_name, subcommand, **kwargs):
        self.subcommand = subcommand
        return super().create_parser(prog_name, subcommand)

    def add_arguments(self, parser):
        super().add_arguments(parser)
        parser.add_argument('--loader', action="store_true")
        parser.add_argument('--test', action="store_true")
        parser.add_argument('--total', default=0)
        parser.add_argument('--encoding', default='utf8')
        parser.add_argument('--logfile', default="%s_%s.log" % (str(self.subcommand).lower(), f"{datetime.datetime.now():%Y%m%d_%H%M%S_%f}"))
        parser.add_argument('--progressbar', action="store_true")
        parser.add_argument('--userlog', default=None)

    def handle(self, *args, **options):
        self.in_test = options.get('test')
        self.encoding = options.get('encoding')
        self.logfile = options.get('logfile')
        self.loader = options.get('loader')
        self.progressbar = options.get('progressbar')
        self.verbosity = options.get('verbosity', 0)
        self.userlog_cache = self.get_user(options.get('userlog'))
        self.logger.debug('start')
        self.makeJob()
        self.showErrors()
        self.logger.debug('end')

    def prepare_request(self):
        class request:
            user = self.userlog_cache
        request_kept.request = request

    def makeJob(self):
        self.prepare_request()
        self.before_job()
        self.do()
        self.after_job()

    def before_job(self): pass
    def after_job(self): pass

    def showErrors(self):
        for error in self.errors:
            self.logger.info(error)

    def do(self):
        raise NotImplementedError("Command should implement method do(self)")

class ModelBaseCommand(BaseCommand):
    help = 'Commande Model Base'
    manager = 'objects'
    label = None
    model = None
    filter = None

    def add_arguments(self, parser):
        super().add_arguments(parser)
        parser.add_argument('--create', action="store_true")
        parser.add_argument('--label', default=None)
        parser.add_argument('--model', default=None)
        parser.add_argument('--filter', default=None)
        parser.add_argument('--manager', default='objects')
        parser.add_argument('--search', action="store_true")

    def handle(self, *args, **options):
        self.create = options.get('create')
        self.label = options.get('label', self.label)
        self.model = options.get('model', self.model)
        self.manager = options.get('manager', self.manager)
        self.filter = options.get('filter')
        self.search = options.get('search')
        super().handle(*args, **options)

    @property
    def model_use(self, *args, **kwargs):
        label = kwargs.get('label', self.label)
        model = kwargs.get('model', self.model)
        return get_model(label, model)

    def get_queryset(self, *args, **kwargs):
        manager = kwargs.get('manager', self.manager)
        model = self.model_use
        return getattr(model, manager).filter(**dict(x.split(',') for x in self.filter.split(';')) if self.filter else {})

    def do(self):
        self.each_objects()

    def each_objects(self):
        qs = self.get_queryset()
        self.total = len(qs)
        for obj in qs:
            self.current_object = obj
            self.set_position()
            if self.loader or self.progressbar:
                self.progress_bar()
            self.on_object(obj)

    def on_object(self, object):
        raise NotImplementedError("Command should implement method on_object(self, obj)")

class ImportModelCommand(ModelBaseCommand):
    _reader = None
    _total = None
    current_row = None
    column_for_current = None
    fields = {}
    reverse = None
    real_values = {}
    required_fields = []
    need_reset_reader = False

    def reset_reader(self):
        self.position = 0
        self.need_reset_reader = True

    def is_required(self, name):
        return (name in self.required_fields)

    def field(self, name):
        try:
            return self.current_row[self.reverse[name]]
        except KeyError:
            for key,value in self.current_row.items():
                if key and key.lower() == name:
                    return self.current_row[key]
        if self.is_required(name):
            raise KeyError(name + " not found")
        return None

    def real_value(self, value):
        if value and value.lower() in self.real_values:
            return self.real_values[value.lower()]
        return value

    @property
    def reader(self):
        raise NotImplementedError("Command should implement property reader")

    @property
    def total(self):
        raise NotImplementedError("Command should implement property total")

    def prepare_fields(self, fields):
        if hasattr(self, 'fields'):
            ofields = self.fields
            self.fields = {}
            for field in fields:
                self.fields[field] = ofields[field] if field in ofields else field
            self.reverse = {v: k for k,v in self.fields.items()}
        else:
            self.fields = self.reverse = {field: field for field in fields}

    def do(self):
        self.loop_qs("on_row")

    def loop_qs(self, do):
        self.prepare_fields(self.reader.fieldnames)
        for row in self.reader:
            self.current_row = row
            self.set_position()
            if self.loader or self.progressbar:
                self.progress_bar()
            getattr(self, do)(row)

    def on_row(self, row):
        raise NotImplementedError("Command should implement method on_object(self, obj)")


class XLSModelCommand(ImportModelCommand):
    @property
    def reader(self):
        if not self._reader or self.need_reset_reader:
            self._reader = ReaderXLS(self.xlsfile, self.sheet)
            self.need_reset_reader = False
        return self._reader

    @property
    def total(self):
        return self.reader.total-1

    def add_arguments(self, parser):
        parser.add_argument('--sheet')
        parser.add_argument('--xls')
        super().add_arguments(parser)

    def handle(self, *args, **options):
        self.xlsfile = options.get('xls')
        print(self.xlsfile)
        self.sheet = options.get('sheet')
        if not os.path.isfile(self.xlsfile):
            raise CommandError('XLS "%s" does not exist' % self.csv)
        super().handle(*args, **options)

class CSVModelCommand(ImportModelCommand):
    def add_arguments(self, parser):
        parser.add_argument('--csv')
        parser.add_argument('--delimiter', default=',')
        parser.add_argument('--quotechar', default='"')
        parser.add_argument('--quoting', default=csv.QUOTE_ALL)
        super().add_arguments(parser)

    def handle(self, *args, **options):
        self.csvfile = options.get('csv')
        self.delimiter = options.get('delimiter')
        self.quotechar = options.get('quotechar')
        self.quoting = options.get('quoting')
        if not os.path.isfile(self.csvfile):
            raise CommandError('CSV "%s" does not exist' % self.csv)
        super().handle(*args, **options)

    @property
    def reader(self):
        if not self._reader or self.need_reset_reader:
            csvfile = open(self.csvfile, encoding=self.encoding)
            self._reader = csv.DictReader(csvfile, delimiter=self.delimiter)
            self.need_reset_reader = False
        return self._reader

    @property
    def total(self):
        if not self._total:
            self._total = len(open(self.csvfile).readlines())-1
        return self._total
