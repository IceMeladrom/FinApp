# Generated by Django 4.0.2 on 2022-03-28 15:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('FinancialApp', '0004_alter_articles_dislikes_alter_articles_lastupdate_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='PassedExams',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('UserID', models.IntegerField()),
                ('ArticleID', models.IntegerField()),
            ],
        ),
    ]