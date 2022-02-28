from django.contrib.auth.models import AbstractUser
from django.contrib.postgres.fields import ArrayField
from django.db import models
from django.urls import reverse
from django.utils.html import format_html


class User(AbstractUser):
    email = models.EmailField(
        verbose_name='email',
        unique=True,
        max_length=255
    )
    first_name = models.CharField(
        verbose_name='name',
        max_length=100
    )
    last_name = models.CharField(
        verbose_name='surname',
        max_length=100
    )
    is_staff = models.BooleanField(
        verbose_name='admin',
        default=False
    )

    class Meta:
        verbose_name = 'user'
        verbose_name_plural = 'users'


class Company(models.Model):
    name = models.CharField(max_length=100)
    profile = models.CharField(max_length=100, null=True)
    description = models.CharField(max_length=100, null=True)
    tags = ArrayField(base_field=models.CharField(max_length=20), null=True)

    class Meta:
        verbose_name = 'company'
        verbose_name_plural = 'companies'

    def __str__(self):
        return self.name

    def withLink(self):
        url = reverse(
            f"admin:{self._meta.app_label}_{self._meta.model_name}_change",
            args=[self.id])
        return format_html(f'<a href={url}>{str(self)}</a>')
