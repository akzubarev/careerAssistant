# Generated by Django 4.0.3 on 2022-03-13 14:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0004_remove_article_relatedarticles_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='article',
            name='relatedArticles',
            field=models.ManyToManyField(to='main.article'),
        ),
    ]