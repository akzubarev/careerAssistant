from django.contrib.auth.models import AbstractUser
from django.contrib.postgres.fields import ArrayField
from django.db import models


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
    profile = models.CharField(max_length=100)
    description = models.CharField(max_length=100)
    tags = ArrayField(base_field=models.CharField(max_length=20))

    class Meta:
        verbose_name = 'company'
        verbose_name_plural = 'companies'