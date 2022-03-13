from django.contrib.postgres.fields import ArrayField
from django.db import models
from django.db.models import SET_NULL, CASCADE
from django.urls import reverse
from django.utils.html import format_html

from apps.recommendations.models import Event
from apps.users.models import Company, User
from config.mixins import AutoCreatedUpdatedMixin


class FormResult(AutoCreatedUpdatedMixin):
    user = models.ForeignKey(to=User, on_delete=SET_NULL,
                             related_name="form_results",
                             null=True, blank=False)
    # company = models.ForeignKey(to=Company, on_delete=SET_NULL,
    #                             null=True, blank=False)
    jobs = models.JSONField(null=True, blank=True)

    skills = models.TextField(null=True, blank=True)

    competitions = models.TextField(null=True, blank=True)

    additional = ArrayField(base_field=models.CharField(max_length=300),
                            null=True, blank=True)

    career_area = models.CharField(max_length=300, null=True, blank=True)

    def __str__(self):
        return f"{self.user}: {self.id}"

    def withLink(self):
        url = reverse(
            f"admin:{self._meta.app_label}_{self._meta.model_name}_change",
            args=[self.id])
        return format_html(f'<a href={url}>{str(self)}</a>')

    class Meta:
        verbose_name = 'form result'
        verbose_name_plural = 'form results'


class ScoringResult(AutoCreatedUpdatedMixin):
    user = models.ForeignKey(to=User, on_delete=SET_NULL,
                             related_name="scoring_results",
                             null=True, blank=False)

    formResult = models.ForeignKey(to=FormResult,
                                   related_name="score",
                                   on_delete=CASCADE, null=True)

    profiles = ArrayField(base_field=models.CharField(max_length=100),
                          null=False, blank=False)

    class Meta:
        verbose_name = 'scoring result'
        verbose_name_plural = 'scoring results'
