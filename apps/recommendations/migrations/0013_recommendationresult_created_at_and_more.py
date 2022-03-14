# Generated by Django 4.0.3 on 2022-03-13 20:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('recommendations', '0012_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='recommendationresult',
            name='created_at',
            field=models.DateTimeField(blank=True, db_index=True, null=True, verbose_name='created at'),
        ),
        migrations.AddField(
            model_name='recommendationresult',
            name='updated_at',
            field=models.DateTimeField(blank=True, db_index=True, null=True, verbose_name='updated at'),
        ),
    ]