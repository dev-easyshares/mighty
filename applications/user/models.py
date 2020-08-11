from django.db import models
from django.conf import settings
from django.contrib.auth.models import AbstractUser
from django.contrib.contenttypes.models import ContentType
from django.contrib.contenttypes.fields import GenericRelation
from django.urls import reverse

from mighty.fields import JSONField
from mighty.models.base import Base
from mighty.models.image import Image
from mighty.functions import masking_email, masking_phone
from mighty.applications.logger.models import ChangeLog
from mighty.applications.address.models import Address
from mighty.applications.user.apps import UserConfig as conf
from mighty.applications.user.manager import UserManager
from mighty.applications.user import translates as _, fields, choices

from phonenumber_field.modelfields import PhoneNumberField
import uuid, logging
logger = logging.getLogger(__name__)

class UserAccessLogModel(ChangeLog):
    object_id = models.ForeignKey(conf.ForeignKey.user, on_delete=models.CASCADE, related_name='user_accesslog')

    class Meta:
        abstract = True

class UserChangeLogModel(ChangeLog):
    object_id = models.ForeignKey(conf.ForeignKey.user, on_delete=models.CASCADE, related_name='user_changelog')

    class Meta:
        abstract = True

class User(AbstractUser, Base, Image):
    search_fields = fields.search
    username = models.CharField(_.username, max_length=254, unique=True, blank=True, null=True)
    email = models.EmailField(_.email, unique=True)
    phone = PhoneNumberField(_.phone, blank=True, null=True, unique=True)
    method = models.CharField(_.method, choices=choices.METHOD, default=choices.METHOD_FRONTEND, max_length=15)
    method_backend = models.CharField(_.method, max_length=255, blank=True, null=True)
    gender = models.CharField(_.gender, max_length=1, choices=choices.GENDER, blank=True, null=True)
    style = models.CharField(max_length=255, default="dark")
    channel = models.CharField(max_length=255, editable=False, blank=True, null=True)

    if 'mighty.applications.messenger':
        missives = GenericRelation(conf.ForeignKey.missive, content_type_field='user_or_invitation')

    if 'mighty.applications.nationality' in settings.INSTALLED_APPS:
        nationalities = models.ManyToManyField(conf.ForeignKey.nationalities, blank=True)

    class Meta(Base.Meta):
        db_table = 'auth_user'
        abstract = True
        verbose_name = _.v_user
        verbose_name_plural = _.vp_user
        ordering = ['last_name', 'first_name', 'email']

    USERNAME_FIELD = conf.Field.username
    REQUIRED_FIELDS = conf.Field.required
    objects = UserManager()

    @property
    def admin_list_url(self):
        return reverse('admin:auth_proxyuser_changelist')

    @property
    def admin_add_url(self):
        return reverse('admin:auth_proxyuser_add')

    @property
    def admin_change_url(self):
        return reverse('admin:auth_proxyuser_change', kwargs={"object_id": self.pk})

    @property
    def admin_disable_url(self):
        return reverse('admin:auth_proxyuser_disable', kwargs={"object_id": self.pk})

    @property
    def admin_enable_url(self):
        return reverse('admin:auth_proxyuser_enable', kwargs={"object_id": self.pk})
    @property
    def fullname(self):
        return "%s %s" % (self.last_name, self.first_name) if all([self.last_name, self.first_name]) else ''

    @property
    def logname(self):
        return '%s.%s' % (self.username, self.id)

    @property
    def representation(self):
        if self.fullname: return self.fullname
        if self.username: return self.username
        if self.email: return self.email
        return ''

    def __str__(self):
        if self.last_name and self.first_name:
            return self.fullname
        return getattr(self, self.USERNAME_FIELD)

    def has_perm(self, perm, obj=None):
        return super().has_perm(perm, obj=None)

    def get_client_ip(self, request):
        ip = request.META.get('HTTP_X_FORWARDED_FOR').split(',')[0] if request.META.get('HTTP_X_FORWARDED_FOR') else request.META.get('REMOTE_ADDR')
        if ip is not None:
            internetprotocol = ContentType.objects.get(app_label='mighty', model='internetprotocol').model_class()
            obj, created = internetprotocol.objects.get_or_create(ip=ip, user=self)
            logger.info('connected from ip: %s' % ip, extra={'user': self})

    def get_user_agent(self, request):
        useragent = ContentType.objects.get(app_label='mighty', model='useragent').model_class()
        obj, created = useragent.objects.get_or_create(useragent=request.META['HTTP_USER_AGENT'], user=self)
        logger.info('usereagent: %s' % request.META['HTTP_USER_AGENT'], extra={'user': self})

    def gen_username(self):
        prefix = "".join([l for l in getattr(self, conf.Field.username) if l.isalpha()])
        prefix = prefix[:3] if len(prefix) >= 3 else prefix
        exist = True
        while exist:
            username = '%s%s' % ('%s-' % prefix if prefix else '', str(uuid.uuid4())[:8])
            username = username.lower()
            try:
                type(self).objects.get(username=username)
            except type(self).DoesNotExist:
                exist = False
        return username

    def save(self, *args, **kwargs):
        if self.email is not None: self.email = self.email.lower()
        if self.username is not None: self.username = self.username.lower()
        else: self.username = self.gen_username()
        super(User, self).save(*args, **kwargs)

class Email(Base):
    user = models.ForeignKey(conf.ForeignKey.user, on_delete=models.CASCADE, related_name='user_email')
    email = models.EmailField(_.email, unique=True)
    default = models.BooleanField(default=False)
    search_fields = ('email',)

    class Meta(Base.Meta):
        abstract = True

    @property
    def masking(self):
        return masking_email(self.email)

class Phone(Base):
    user = models.ForeignKey(conf.ForeignKey.user, on_delete=models.CASCADE, related_name='user_phone')
    phone = PhoneNumberField(_.phone, unique=True)
    default = models.BooleanField(default=False)
    search_fields = ('phone',)

    class Meta(Base.Meta):
        abstract = True

    @property
    def masking(self):
        return masking_phone(self.phone)

class UserAddress(Address):
    user = models.ForeignKey(conf.ForeignKey.user, on_delete=models.CASCADE, related_name='user_address')

    class Meta(Base.Meta):
        abstract = True

    @property
    def masking(self):
        return "**"

class InternetProtocol(models.Model):
    user = models.ForeignKey(conf.ForeignKey.user, on_delete=models.CASCADE, related_name='user_ip')
    ip = models.GenericIPAddressField(editable=False)

    class Meta(Base.Meta):
        abstract = True

class UserAgent(models.Model):
    user = models.ForeignKey(conf.ForeignKey.user, on_delete=models.CASCADE, related_name='user_useragent')
    useragent = models.CharField(max_length=255, editable=False)

    class Meta(Base.Meta):
        abstract = True

class UserOrInvitation(Base):
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    email = models.EmailField(_.email, unique=True)
    phone = PhoneNumberField(_.phone, blank=True, null=True, unique=True)
    user = models.ForeignKey(conf.ForeignKey.user, on_delete=models.CASCADE, related_name='userorinvitation_user', blank=True, null=True)
    status = models.CharField(max_length=8, choices=choices.STATUS, default=choices.STATUS_PENDING)

    class Meta(Base.Meta):
        db_table = 'auth_userorinvitation'
        abstract = True
        verbose_name = _.v_userorinvitation
        verbose_name_plural = _.vp_userorinvitation
        ordering = ['last_name', 'first_name', 'email']

    if 'mighty.applications.messenger':
        missives = GenericRelation(conf.ForeignKey.missive, content_type_field='user_or_invitation')

    @classmethod
    def from_db(self, db, field_names, values):
        instance = super().from_db(db, field_names, values)
        if instance.user:
            instance.user.status = instance.status
            instance.user.user = instance.user
            instance = instance.user
        return instance

    def __str__(self):
        return str(self.user) if self.user else '%s %s (%s)' % (self.first_name, self.last_name, self.masking_email)

    @property
    def logname(self): 
        return self.user.logname if self.user else 'user_invitation.%s' % self.id

    @property
    def masking_email(self):
        return masking_email(self.email)

    @property
    def masking_phone(self):
        return masking_phone(self.phone)

    class Meta(Base.Meta):
        abstract = True

    def save(self, *args, **kwargs):
        self.status = choices.STATUS_ACCEPTED if self.user else self.status
        super().save(*args, **kwargs)
        #if not self.missives.count():
        #    self.missives.create(**{
        #        "user_or_invitation": self.missives.content_type,
        #        "object_id": self.id,
        #        "target": self.email,
        #        "subject": 'subject: Invitation',
        #        "html": "html: Invitation",
        #        "txt": "txt: Invitation",
        #    })