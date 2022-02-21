from django.db import models
from django.utils import timezone


# Create your models here.
class Users(models.Model):
    Login = models.TextField(unique=True)
    Password = models.TextField()
    Email = models.EmailField(unique=True)
    Amount = models.IntegerField(default=0)
    Name = models.TextField()
    Surname = models.TextField()


class Statistics(models.Model):
    UserID = models.IntegerField()
    Amount = models.IntegerField()
    Date = models.DateTimeField(default=timezone.now)
    Category = models.TextField()
