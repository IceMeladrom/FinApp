# Generated by Django 4.0.2 on 2022-03-28 14:46

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('FinancialApp', '0003_rename_article_articles_text'),
    ]

    operations = [
        migrations.AlterField(
            model_name='articles',
            name='Dislikes',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='articles',
            name='LastUpdate',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
        migrations.AlterField(
            model_name='articles',
            name='Likes',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='articles',
            name='Visits',
            field=models.IntegerField(default=0),
        ),
    ]