# Generated by Django 4.0.2 on 2022-03-01 17:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('FinancialApp', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='users',
            name='Avatar',
            field=models.ImageField(default='img/Durr.png', null=True, upload_to='img/'),
        ),
    ]