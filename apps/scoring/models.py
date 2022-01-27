from django.db import models
from django.db.models import SET_NULL

from apps.users.models import Company, User


class ScoringResult(models.Model):
    user = models.ForeignKey(to=User, on_delete=SET_NULL,
                             null=True, blank=False)
    company = models.ForeignKey(to=Company, on_delete=SET_NULL,
                                null=True, blank=False)
    profile = models.CharField(max_length=100)
    position = models.CharField(max_length=100)
    experience = models.IntegerField(help_text="Количество месяцев")
    education = models.CharField(max_length=100)
    scores = models.JSONField()
    preferences = models.JSONField()

    class Meta:
        verbose_name = 'scoring result'
        verbose_name_plural = 'scoring results'
