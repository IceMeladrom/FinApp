# Generated by Django 4.0.2 on 2022-02-21 17:26

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('FinancialApp', '0002_alter_statistics_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='statistics',
            name='Date',
            field=models.DateTimeField(default=django.utils.timezone.now, null=True),
        ),
    ]
