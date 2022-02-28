# Generated by Django 4.0.2 on 2022-02-28 20:29

import django.contrib.postgres.fields
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0002_alter_company_options'),
        ('scoring', '0003_alter_scoringresult_options_scoringresult_user'),
        ('recommendations', '0003_alter_article_options_alter_course_options_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='article',
            name='description',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='article',
            name='link',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='article',
            name='name',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='article',
            name='profile',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='article',
            name='relatedArticles',
            field=models.ManyToManyField(null=True, to='recommendations.Article'),
        ),
        migrations.AlterField(
            model_name='article',
            name='rubric',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='article',
            name='tags',
            field=django.contrib.postgres.fields.ArrayField(base_field=models.CharField(max_length=20), null=True, size=None),
        ),
        migrations.AlterField(
            model_name='course',
            name='description',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='course',
            name='link',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='course',
            name='name',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='course',
            name='profile',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='course',
            name='tags',
            field=django.contrib.postgres.fields.ArrayField(base_field=models.CharField(max_length=20), null=True, size=None),
        ),
        migrations.AlterField(
            model_name='course',
            name='type',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='event',
            name='city',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='event',
            name='company',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='users.company'),
        ),
        migrations.AlterField(
            model_name='event',
            name='date',
            field=models.DateTimeField(null=True),
        ),
        migrations.AlterField(
            model_name='event',
            name='description',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='event',
            name='link',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='event',
            name='name',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='event',
            name='profile',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='event',
            name='tags',
            field=django.contrib.postgres.fields.ArrayField(base_field=models.CharField(max_length=20), null=True, size=None),
        ),
        migrations.AlterField(
            model_name='event',
            name='type',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='recommendationresult',
            name='articles',
            field=models.ManyToManyField(null=True, to='recommendations.Article'),
        ),
        migrations.AlterField(
            model_name='recommendationresult',
            name='courses',
            field=models.ManyToManyField(null=True, to='recommendations.Course'),
        ),
        migrations.AlterField(
            model_name='recommendationresult',
            name='events',
            field=models.ManyToManyField(null=True, to='recommendations.Event'),
        ),
        migrations.AlterField(
            model_name='recommendationresult',
            name='scoringResult',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='scoring.scoringresult'),
        ),
        migrations.AlterField(
            model_name='recommendationresult',
            name='vacancies',
            field=models.ManyToManyField(null=True, to='recommendations.Vacancy'),
        ),
        migrations.AlterField(
            model_name='vacancy',
            name='branch',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='vacancy',
            name='city',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='vacancy',
            name='company',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='users.company'),
        ),
        migrations.AlterField(
            model_name='vacancy',
            name='description',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='vacancy',
            name='experience',
            field=models.IntegerField(help_text='Количество месяцев', null=True),
        ),
        migrations.AlterField(
            model_name='vacancy',
            name='link',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='vacancy',
            name='name',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='vacancy',
            name='profession',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='vacancy',
            name='profile',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='vacancy',
            name='shift',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='vacancy',
            name='tags',
            field=django.contrib.postgres.fields.ArrayField(base_field=models.CharField(max_length=20), null=True, size=None),
        ),
        migrations.AlterField(
            model_name='vacancy',
            name='type',
            field=models.CharField(max_length=100, null=True),
        ),
    ]
