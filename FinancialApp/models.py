import datetime

from django.db import models


# Create your models here.
class User(models.Model):
    Nickname = models.TextField(unique=True)
    Password = models.TextField()
    Amount = models.IntegerField(default=0)


class Statistic(models.Model):
    UserID = models.IntegerField()
    Amount = models.IntegerField()
    Date = models.DateTimeField(default=datetime.date.today())
    Category = models.TextField()
