# Generated by Django 4.0.2 on 2022-03-28 14:01

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('FinancialApp', '0002_articles_exams'),
    ]

    operations = [
        migrations.RenameField(
            model_name='articles',
            old_name='Article',
            new_name='Text',
        ),
    ]