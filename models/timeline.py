from django.db import models
from mighty.models.base import Base
from mighty import translates as _
from datetime import datetime

class TimelineModel(Base):
    object_id = models.ForeignKey('', on_delete=models.CASCADE)
    field = models.CharField(_.field, max_length=255, db_index=True)
    value = models.BinaryField(_.value)
    fmodel = models.CharField(_.fmodel, max_length=255)
    date_begin = models.DateField(_.date_begin)
    date_end = models.DateField(_.date_end, null=True, blank=True)
    user = models.CharField(max_length=255)
    to_init = False

    class Meta:
        abstract = True
        verbose_name = _.v_timeline
        verbose_name_plural = _.vp_timeline
        ordering = ['-date_begin']
        unique_together = ['date_begin', 'value']

    @property
    def get_value(self):
        return bytes(self.value).decode('utf-8')

    @property
    def is_init(self):
        return type(self).objects.filter(object_id=self.object_id, field=self.field).first()

    def replace_value(self):
        setattr(self.object_id, self.field, self.get_value)
        self.object_id.save()

    def save(self, *args, **kwargs):
        first = self.is_init
        if not first and not self.to_init:
            init = type(self)(
                object_id=self.object_id,
                field=self.field,
                value=bytes(str(getattr(self.object_id, self.field)), 'utf-8'),
                date_begin=self.object_id.date_create,
                date_end=self.date_begin
            )
            init.to_init = True
            init.save()
        last = type(self).objects.filter(object_id=self.object_id, field=self.field, date_end__isnull=True)
        last.update(date_end=self.date_begin)
        self.replace_value()
        super().save(*args, **kwargs)
