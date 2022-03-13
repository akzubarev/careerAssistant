from django.db import models
from django.db.models import CASCADE

from apps.main.models import Event, Article, Course, Vacancy
from apps.scoring.models import ScoringResult
from apps.users.models import Company, User
from config.mixins import AutoCreatedUpdatedMixin


class RecommendationResult(AutoCreatedUpdatedMixin):
    scoringResult = models.ForeignKey(to=ScoringResult,
                                      related_name="recommendation",
                                      on_delete=CASCADE, null=True)
    events = models.ManyToManyField(to=Event,
                                    related_name="recommendations")
    articles = models.ManyToManyField(to=Article,
                                      related_name="recommendations")
    courses = models.ManyToManyField(to=Course,
                                     related_name="recommendations")
    vacancies = models.ManyToManyField(to=Vacancy,
                                       related_name="recommendations")

    class Meta:
        verbose_name = 'recommendation result'
        verbose_name_plural = 'recommendation results'
