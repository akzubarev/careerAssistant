# Generated by Django 4.0.3 on 2022-03-13 12:41

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
    dependencies = [
        ('scoring', '0003_alter_scoringresult_options_scoringresult_user'),
        ('recommendations', '0009_alter_event_city_alter_event_type'),
    ]

    operations = [
        migrations.AlterField(
            model_name='recommendationresult',
            name='scoringResult',
            field=models.ForeignKey(
                null=True,
                on_delete=django.db.models.deletion.CASCADE,
                related_name='recommendation',
                to='scoring.scoringresult'),
        ),
    ]