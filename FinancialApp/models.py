from django.db import models

# Create your models here.
from django.utils.timezone import now


class Users(models.Model):
    Login = models.TextField(unique=True)
    Password = models.TextField()
    Email = models.EmailField(unique=True)
    Amount = models.IntegerField(default=0)
    Name = models.TextField()
    Surname = models.TextField()
    Avatar = models.ImageField(upload_to='img/', null=True, default='img/Durr.png')


class Statistics(models.Model):
    UserID = models.IntegerField()
    CurrentAmount = models.IntegerField()
    Amount = models.IntegerField()
    Date = models.DateTimeField(default=now, editable=False)
    Category = models.TextField()
