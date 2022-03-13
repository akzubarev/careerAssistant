from django.contrib.postgres.indexes import BrinIndex
from django.db import models
from django.utils.timezone import now


class AutoCreatedUpdatedMixin(models.Model):
    created_at = models.DateTimeField(
        verbose_name='created at', unique=False,
        null=True, blank=True, db_index=True,
    )

    updated_at = models.DateTimeField(
        verbose_name='updated at', unique=False,
        null=True, blank=True, db_index=True,
    )

    class Meta:
        abstract = True
        indexes = (BrinIndex(fields=['created_at']),)

    def save(self, *args, **kwargs):
        if kwargs.get('update_fields'):
            if 'updated_at' not in kwargs['update_fields']:
                kwargs['update_fields'].append('updated_at')

        if not self.id or not self.created_at:
            self.created_at = now()
            self.updated_at = self.created_at
        else:
            self.updated_at = now()
        super(AutoCreatedUpdatedMixin, self).save(*args, **kwargs)
