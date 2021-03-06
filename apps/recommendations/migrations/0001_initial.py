# Generated by Django 3.2.9 on 2021-12-02 18:14

import django.contrib.postgres.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Article',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('profile', models.CharField(max_length=100)),
                ('description', models.CharField(max_length=100)),
                ('tags', django.contrib.postgres.fields.ArrayField(base_field=models.CharField(max_length=20), size=None)),
                ('link', models.CharField(max_length=100)),
                ('rubric', models.CharField(max_length=100)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Course',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('profile', models.CharField(max_length=100)),
                ('description', models.CharField(max_length=100)),
                ('tags', django.contrib.postgres.fields.ArrayField(base_field=models.CharField(max_length=20), size=None)),
                ('link', models.CharField(max_length=100)),
                ('type', models.CharField(max_length=100)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Event',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('profile', models.CharField(max_length=100)),
                ('description', models.CharField(max_length=100)),
                ('tags', django.contrib.postgres.fields.ArrayField(base_field=models.CharField(max_length=20), size=None)),
                ('link', models.CharField(max_length=100)),
                ('type', models.CharField(max_length=100)),
                ('date', models.DateTimeField()),
                ('city', models.CharField(max_length=100)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Vacancy',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('profile', models.CharField(max_length=100)),
                ('description', models.CharField(max_length=100)),
                ('tags', django.contrib.postgres.fields.ArrayField(base_field=models.CharField(max_length=20), size=None)),
                ('link', models.CharField(max_length=100)),
                ('profession', models.CharField(max_length=100)),
                ('branch', models.CharField(max_length=100)),
                ('experience', models.IntegerField(help_text='???????????????????? ??????????????')),
                ('type', models.CharField(max_length=100)),
                ('shift', models.CharField(max_length=100)),
                ('city', models.CharField(max_length=100)),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
