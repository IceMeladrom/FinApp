# Generated by Django 4.0.2 on 2022-02-28 18:30

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Statistics',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('UserID', models.IntegerField()),
                ('Amount', models.IntegerField()),
                ('Date', models.DateTimeField(default=django.utils.timezone.now, null=True)),
                ('Category', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='Users',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Login', models.TextField(unique=True)),
                ('Password', models.TextField()),
                ('Email', models.EmailField(max_length=254, unique=True)),
                ('Amount', models.IntegerField(default=0)),
                ('Name', models.TextField()),
                ('Surname', models.TextField()),
                ('Avatar', models.ImageField(null=True, upload_to='img/')),
            ],
        ),
    ]
