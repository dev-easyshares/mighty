from django.db import models
from django.template.defaultfilters import slugify

from mighty.apps import MightyConfig as conf
from mighty.models.base import Base
from mighty.applications.shop import generate_code_service, generate_code_offer, choices

class Service(Base):
    name = models.CharField(max_length=255)
    code = models.CharField(max_length=50, default=generate_code_service, unique=True)

    class Meta(Base.Meta):
        abstract = True
        ordering = ['name']

    def __str__(self):
        return "%s(%s)" % (self.name, self.code)

class Offer(Base):
    named_id = models.CharField(max_length=255, db_index=True, null=True, editable=False)
    name = models.CharField(max_length=255)
    frequency = models.CharField(max_length=255, choices=choices.FREQUENCIES, default='MONTH')
    duration = models.DurationField(blank=True, null=True, editable=False)
    price = models.FloatField()
    service = models.ManyToManyField('mighty.Service', blank=True, related_name='service_offer')
    price_tenant = models.FloatField(default=0.0)
    is_custom = models.BooleanField(default=False)
    code = models.CharField(max_length=50, default=generate_code_offer, unique=True)

    class Meta(Base.Meta):
        abstract = True
        ordering = ['name']

    def __str__(self):
        return "%s (%s)" % (self.name, self.get_frequency_display())

    def set_named_id(self):
        self.named_id = conf.named_tpl % {"named": slugify(self.name), "id": self.id}

    def pre_update(self):
        self.set_named_id()

    def post_create(self):
        if not self.named_id:
            self.save()