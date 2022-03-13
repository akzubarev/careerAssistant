from django.contrib.postgres.fields import ArrayField
from django.db import models
from django.db.models import CASCADE

from apps.users.models import Company


class Recommendation(models.Model):
    name = models.CharField(max_length=500, null=True)
    profile = models.CharField(max_length=500, null=True)
    description = models.CharField(max_length=1000, null=True)
    tags = ArrayField(base_field=models.CharField(max_length=20), null=True)
    link = models.CharField(max_length=500, null=True)

    class Meta:
        abstract = True

    def __str__(self):
        return self.name


class Event(Recommendation):
    type = models.CharField(max_length=500, null=True)
    date = models.DateTimeField(null=True)
    company = models.ForeignKey(to=Company, on_delete=CASCADE, null=True)
    city = models.CharField(max_length=500, null=True)

    class Meta:
        verbose_name = 'event'
        verbose_name_plural = 'events'


class Article(Recommendation):
    relatedArticles = models.ManyToManyField(to="self")
    rubric = models.CharField(max_length=100, null=True)

    class Meta:
        verbose_name = 'article'
        verbose_name_plural = 'articles'


class Course(Recommendation):
    type = models.CharField(max_length=100, null=True)

    class Meta:
        verbose_name = 'course'
        verbose_name_plural = 'courses'


class Vacancy(Recommendation):
    company = models.ForeignKey(to=Company, on_delete=CASCADE, null=True)
    profession = models.CharField(max_length=500, null=True)
    branch = models.CharField(max_length=100, null=True)
    experience = models.IntegerField(help_text="Количество месяцев", null=True)
    type = models.CharField(max_length=100, null=True)
    shift = models.CharField(max_length=100, null=True)
    city = models.CharField(max_length=100, null=True)

    class Meta:
        verbose_name = 'vacancy'
        verbose_name_plural = 'vacancies'
