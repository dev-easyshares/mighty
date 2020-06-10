# Generated by Django 3.0.7 on 2020-06-10 10:44

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone
import jsonfield.fields
import mighty.applications.user.manager
import mighty.functions
import mighty.models.base
import phonenumber_field.modelfields
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('contenttypes', '0002_remove_content_type_name'),
        ('auth', '0012_twofactor'),
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('is_superuser', models.BooleanField(default=False, help_text='Designates that this user has all permissions without explicitly assigning them.', verbose_name='superuser status')),
                ('first_name', models.CharField(blank=True, max_length=30, verbose_name='first name')),
                ('last_name', models.CharField(blank=True, max_length=150, verbose_name='last name')),
                ('is_staff', models.BooleanField(default=False, help_text='Designates whether the user can log into this admin site.', verbose_name='staff status')),
                ('is_active', models.BooleanField(default=True, help_text='Designates whether this user should be treated as active. Unselect this instead of deleting accounts.', verbose_name='active')),
                ('date_joined', models.DateTimeField(default=django.utils.timezone.now, verbose_name='date joined')),
                ('uid', models.UUIDField(default=uuid.uuid4, editable=False, unique=True)),
                ('logfields', jsonfield.fields.JSONField(blank=True, default=mighty.models.base.default_logfield_dict, null=True)),
                ('is_disable', models.BooleanField(default=False, editable=False, verbose_name='Is disable')),
                ('search', models.TextField(blank=True, db_index=True, null=True)),
                ('date_create', models.DateTimeField(auto_now_add=True, verbose_name='Creation date')),
                ('create_by', models.CharField(blank=True, editable=False, max_length=254, null=True, verbose_name='Created by')),
                ('date_update', models.DateTimeField(auto_now=True, verbose_name='Update date')),
                ('update_by', models.CharField(blank=True, editable=False, max_length=254, null=True, verbose_name='Updated by')),
                ('image', models.ImageField(blank=True, null=True, upload_to=mighty.functions.image_directory_path)),
                ('username', models.CharField(blank=True, max_length=254, null=True, unique=True, verbose_name='Username')),
                ('email', models.EmailField(max_length=254, unique=True, verbose_name='Email')),
                ('phone', phonenumber_field.modelfields.PhoneNumberField(blank=True, max_length=128, null=True, region=None, unique=True, verbose_name='Phone')),
                ('method', models.CharField(choices=[('CREATESUPERUSER', 'Manage.py createsuperuser'), ('BACKEND', 'Backend (/admin)'), ('FRONTEND', 'Workflow allowed by your website'), ('IMPORT', 'By import')], default='FRONTEND', max_length=15, verbose_name='Creation method')),
                ('method_backend', models.CharField(blank=True, max_length=255, null=True, verbose_name='Creation method')),
                ('gender', models.CharField(blank=True, choices=[('M', 'Homme'), ('W', 'Femme')], max_length=1, null=True, verbose_name='Genre')),
                ('style', models.CharField(default='dark', max_length=255)),
                ('channel', models.CharField(blank=True, editable=False, max_length=255, null=True)),
                ('groups', models.ManyToManyField(blank=True, help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.', related_name='user_set', related_query_name='user', to='auth.Group', verbose_name='groups')),
            ],
            options={
                'verbose_name': 'user',
                'verbose_name_plural': 'users',
                'db_table': 'auth_user',
                'ordering': ['last_name', 'first_name', 'email'],
                'abstract': False,
                'default_permissions': ['add', 'change', 'detail', 'delete', 'disable', 'enable', 'export', 'filter_lvl0', 'filter_lvl1', 'filter_lvl2', 'import', 'list'],
            },
            managers=[
                ('objects', mighty.applications.user.manager.UserManager()),
            ],
        ),
        migrations.CreateModel(
            name='Nationality',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('uid', models.UUIDField(default=uuid.uuid4, editable=False, unique=True)),
                ('logfields', jsonfield.fields.JSONField(blank=True, default=mighty.models.base.default_logfield_dict, null=True)),
                ('is_disable', models.BooleanField(default=False, editable=False, verbose_name='Is disable')),
                ('search', models.TextField(blank=True, db_index=True, null=True)),
                ('date_create', models.DateTimeField(auto_now_add=True, verbose_name='Creation date')),
                ('create_by', models.CharField(blank=True, editable=False, max_length=254, null=True, verbose_name='Created by')),
                ('date_update', models.DateTimeField(auto_now=True, verbose_name='Update date')),
                ('update_by', models.CharField(blank=True, editable=False, max_length=254, null=True, verbose_name='Updated by')),
                ('image', models.ImageField(blank=True, null=True, upload_to=mighty.functions.image_directory_path)),
                ('country', models.CharField(max_length=255, verbose_name='country')),
                ('alpha2', models.CharField(max_length=2, verbose_name='alpha2')),
                ('alpha3', models.CharField(blank=True, max_length=3, null=True, verbose_name='alpha3')),
                ('numeric', models.CharField(blank=True, max_length=3, null=True, verbose_name='numeric')),
                ('numbering', models.PositiveSmallIntegerField(blank=True, null=True, verbose_name='numbering')),
            ],
            options={
                'verbose_name': 'nationality',
                'verbose_name_plural': 'nationalities',
                'ordering': ['country'],
                'abstract': False,
                'default_permissions': ['add', 'change', 'detail', 'delete', 'disable', 'enable', 'export', 'filter_lvl0', 'filter_lvl1', 'filter_lvl2', 'import', 'list'],
            },
        ),
        migrations.CreateModel(
            name='UserAgent',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('useragent', models.CharField(editable=False, max_length=255)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='user_useragent', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'abstract': False,
                'default_permissions': ['add', 'change', 'detail', 'delete', 'disable', 'enable', 'export', 'filter_lvl0', 'filter_lvl1', 'filter_lvl2', 'import', 'list'],
            },
        ),
        migrations.CreateModel(
            name='UserAddress',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('uid', models.UUIDField(default=uuid.uuid4, editable=False, unique=True)),
                ('logfields', jsonfield.fields.JSONField(blank=True, default=mighty.models.base.default_logfield_dict, null=True)),
                ('is_disable', models.BooleanField(default=False, editable=False, verbose_name='Is disable')),
                ('search', models.TextField(blank=True, db_index=True, null=True)),
                ('date_create', models.DateTimeField(auto_now_add=True, verbose_name='Creation date')),
                ('create_by', models.CharField(blank=True, editable=False, max_length=254, null=True, verbose_name='Created by')),
                ('date_update', models.DateTimeField(auto_now=True, verbose_name='Update date')),
                ('update_by', models.CharField(blank=True, editable=False, max_length=254, null=True, verbose_name='Updated by')),
                ('default', models.BooleanField(default=False)),
                ('street_number', models.PositiveIntegerField(blank=True, null=True, verbose_name='street number')),
                ('way', models.CharField(blank=True, choices=[('ALL', 'Allée'), ('AV', 'Avenue'), ('BD', 'Boulevard'), ('CAR', 'Carrefour'), ('CHS', 'Chaussée'), ('CHE', 'Chemin'), ('CITE', 'Cité'), ('COR', 'Corniche'), ('CRS', 'Cours'), ('DSC', 'Descente'), ('DOM', 'Domaine'), ('ECA', 'Ecart'), ('ESP', 'Esplanade'), ('FG', 'Faubourg'), ('GR', 'Grande Rue'), ('HLE', 'Halle'), ('HAM', 'Hameau'), ('IMP', 'Impasse'), ('LD', 'Lieu-dit'), ('LOT', 'Lotissement'), ('MAR', 'Marché'), ('MTE', 'Montée'), ('PRV', 'Parvis'), ('PAS', 'Passage'), ('PL', 'Place'), ('PLN', 'Plaine'), ('PLT', 'Plateau'), ('PRO', 'Promenade'), ('QUAI', 'Quai'), ('QUA', 'Quartier'), ('ROC', 'Rocade'), ('RPT', 'Rond-point'), ('RTE', 'Route'), ('RUE', 'Rue'), ('RLE', 'Ruelle'), ('RES', 'Résidence'), ('SEN', 'Sente - Sentier'), ('SQ', 'Square'), ('TPL', 'Terre-plein'), ('TRA', 'Traverse'), ('VLA', 'Villa'), ('VLGE', 'Village')], max_length=4, null=True, verbose_name='way')),
                ('route', models.CharField(blank=True, max_length=255, null=True, verbose_name='route')),
                ('locality', models.CharField(blank=True, max_length=255, null=True, verbose_name='locality')),
                ('postal_code', models.CharField(blank=True, max_length=255, null=True, verbose_name='postal code')),
                ('state', models.CharField(blank=True, max_length=255, null=True, verbose_name='state')),
                ('state_code', models.CharField(blank=True, max_length=255, null=True, verbose_name='state code')),
                ('country', models.CharField(blank=True, max_length=255, null=True, verbose_name='country')),
                ('country_code', models.CharField(blank=True, max_length=255, null=True, verbose_name='country code')),
                ('cedex', models.CharField(blank=True, max_length=255, null=True, verbose_name='cedex')),
                ('cedex_code', models.CharField(blank=True, max_length=255, null=True, verbose_name='cedex code')),
                ('special', models.CharField(blank=True, max_length=255, null=True)),
                ('complement', models.CharField(blank=True, max_length=255, null=True)),
                ('index', models.CharField(blank=True, max_length=255, null=True)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='user_address', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'Address',
                'verbose_name_plural': 'Addresses',
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Phone',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('uid', models.UUIDField(default=uuid.uuid4, editable=False, unique=True)),
                ('logfields', jsonfield.fields.JSONField(blank=True, default=mighty.models.base.default_logfield_dict, null=True)),
                ('is_disable', models.BooleanField(default=False, editable=False, verbose_name='Is disable')),
                ('search', models.TextField(blank=True, db_index=True, null=True)),
                ('date_create', models.DateTimeField(auto_now_add=True, verbose_name='Creation date')),
                ('create_by', models.CharField(blank=True, editable=False, max_length=254, null=True, verbose_name='Created by')),
                ('date_update', models.DateTimeField(auto_now=True, verbose_name='Update date')),
                ('update_by', models.CharField(blank=True, editable=False, max_length=254, null=True, verbose_name='Updated by')),
                ('phone', phonenumber_field.modelfields.PhoneNumberField(max_length=128, region=None, unique=True, verbose_name='Phone')),
                ('default', models.BooleanField(default=False)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='user_phone', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'abstract': False,
                'default_permissions': ['add', 'change', 'detail', 'delete', 'disable', 'enable', 'export', 'filter_lvl0', 'filter_lvl1', 'filter_lvl2', 'import', 'list'],
            },
        ),
        migrations.CreateModel(
            name='Log',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('args', models.CharField(blank=True, max_length=255, null=True, verbose_name='The tuple of arguments merged into msg to produce message, or a dict whose values are used for the merge (when there is only one argument, and it is a dictionary).')),
                ('created', models.DateTimeField(auto_now_add=True, verbose_name='Time when the LogRecord was created (as returned by time.time()).')),
                ('exc_info', models.CharField(blank=True, max_length=255, null=True, verbose_name='Exception tuple (à la sys.exc_info) or, if no exception has occurred, None.')),
                ('filename', models.CharField(blank=True, max_length=255, null=True, verbose_name='Filename portion of pathname.')),
                ('funcName', models.CharField(blank=True, max_length=255, null=True, verbose_name='Name of function containing the logging call.')),
                ('levelno', models.PositiveSmallIntegerField(blank=True, null=True, verbose_name='Numeric logging level for the message (DEBUG, INFO, WARNING, ERROR, CRITICAL).')),
                ('lineno', models.CharField(blank=True, max_length=255, null=True, verbose_name='Source line number where the logging call was issued (if available).')),
                ('module', models.CharField(blank=True, max_length=255, null=True, verbose_name='Module (name portion of filename).')),
                ('msecs', models.CharField(blank=True, max_length=255, null=True, verbose_name='Millisecond portion of the time when the LogRecord was created.')),
                ('msg', models.CharField(blank=True, max_length=255, null=True, verbose_name="The format string passed in the original logging call. Merged with args to produce message, or an arbitrary object (see Utilisation d'objets arbitraires comme messages).")),
                ('name', models.CharField(blank=True, max_length=255, null=True, verbose_name='Name of the logger used to log the call.')),
                ('pathname', models.CharField(blank=True, max_length=255, null=True, verbose_name='Full pathname of the source file where the logging call was issued (if available).')),
                ('process', models.CharField(blank=True, max_length=255, null=True, verbose_name='Process ID (if available).')),
                ('processName', models.CharField(blank=True, max_length=255, null=True, verbose_name='Process name (if available).')),
                ('relativeCreated', models.CharField(blank=True, max_length=255, null=True, verbose_name='Time in milliseconds when the LogRecord was created, relative to the time the logging module was loaded.')),
                ('stack_info', models.TextField(blank=True, max_length=255, null=True, verbose_name='Stack frame information (where available) from the bottom of the stack in the current thread, up to and including the stack frame of the logging call which resulted in the creation of this record.')),
                ('thread', models.CharField(blank=True, max_length=255, null=True, verbose_name='Thread ID (if available).')),
                ('object_id', models.PositiveIntegerField()),
                ('content_type', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='contenttypes.ContentType')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='InternetProtocol',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ip', models.GenericIPAddressField(editable=False)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='user_ip', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'abstract': False,
                'default_permissions': ['add', 'change', 'detail', 'delete', 'disable', 'enable', 'export', 'filter_lvl0', 'filter_lvl1', 'filter_lvl2', 'import', 'list'],
            },
        ),
        migrations.CreateModel(
            name='Email',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('uid', models.UUIDField(default=uuid.uuid4, editable=False, unique=True)),
                ('logfields', jsonfield.fields.JSONField(blank=True, default=mighty.models.base.default_logfield_dict, null=True)),
                ('is_disable', models.BooleanField(default=False, editable=False, verbose_name='Is disable')),
                ('search', models.TextField(blank=True, db_index=True, null=True)),
                ('date_create', models.DateTimeField(auto_now_add=True, verbose_name='Creation date')),
                ('create_by', models.CharField(blank=True, editable=False, max_length=254, null=True, verbose_name='Created by')),
                ('date_update', models.DateTimeField(auto_now=True, verbose_name='Update date')),
                ('update_by', models.CharField(blank=True, editable=False, max_length=254, null=True, verbose_name='Updated by')),
                ('email', models.EmailField(max_length=254, unique=True, verbose_name='Email')),
                ('default', models.BooleanField(default=False)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='user_email', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'abstract': False,
                'default_permissions': ['add', 'change', 'detail', 'delete', 'disable', 'enable', 'export', 'filter_lvl0', 'filter_lvl1', 'filter_lvl2', 'import', 'list'],
            },
        ),
        migrations.AddField(
            model_name='user',
            name='nationalities',
            field=models.ManyToManyField(blank=True, to='mighty.Nationality'),
        ),
        migrations.AddField(
            model_name='user',
            name='user_permissions',
            field=models.ManyToManyField(blank=True, help_text='Specific permissions for this user.', related_name='user_set', related_query_name='user', to='auth.Permission', verbose_name='user permissions'),
        ),
    ]
