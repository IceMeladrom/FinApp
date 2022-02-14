import datetime

from django.db import models


# Create your models here.
class Users(models.Model):
    Nickname = models.TextField(unique=True)
    Password = models.TextField()
    Email = models.EmailField()
    Amount = models.IntegerField(default=0)


class Statistics(models.Model):
    UserID = models.IntegerField()
    Amount = models.IntegerField()
    Date = models.DateTimeField(default=datetime.date.today())
    Category = models.TextField()
