from django.contrib.postgres.fields import ArrayField
from django.db import models
from django.db.models import CASCADE

from apps.scoring.models import ScoringResult
from apps.users.models import Company, User


class Recommendation(models.Model):
    name = models.CharField(max_length=100)
    profile = models.CharField(max_length=100)
    description = models.CharField(max_length=100)
    tags = ArrayField(base_field=models.CharField(max_length=20))
    link = models.CharField(max_length=100)

    class Meta:
        abstract = True

    def __str__(self):
        return self.name


class Event(Recommendation):
    type = models.CharField(max_length=100)
    date = models.DateTimeField()
    company = models.ForeignKey(to=Company, on_delete=CASCADE)
    city = models.CharField(max_length=100)

    class Meta:
        verbose_name = 'event'
        verbose_name_plural = 'events'


class Article(Recommendation):
    relatedArticles = models.ManyToManyField(to="self")
    rubric = models.CharField(max_length=100)

    class Meta:
        verbose_name = 'article'
        verbose_name_plural = 'articles'


class Course(Recommendation):
    type = models.CharField(max_length=100)

    class Meta:
        verbose_name = 'course'
        verbose_name_plural = 'courses'


class Vacancy(Recommendation):
    company = models.ForeignKey(to=Company, on_delete=CASCADE)
    profession = models.CharField(max_length=100)
    branch = models.CharField(max_length=100)
    experience = models.IntegerField(help_text="Количество месяцев")
    type = models.CharField(max_length=100)
    shift = models.CharField(max_length=100)
    city = models.CharField(max_length=100)

    class Meta:
        verbose_name = 'vacancy'
        verbose_name_plural = 'vacancies'


class RecommendationResult(models.Model):
    scoringResult = models.ForeignKey(to=ScoringResult, on_delete=CASCADE)
    events = models.ManyToManyField(to=Event)
    articles = models.ManyToManyField(to=Article)
    courses = models.ManyToManyField(to=Course)
    vacancies = models.ManyToManyField(to=Vacancy)

    class Meta:
        verbose_name = 'recommendation result'
        verbose_name_plural = 'recommendation results'
