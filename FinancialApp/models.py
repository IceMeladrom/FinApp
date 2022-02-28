from django.db import models
from django.utils.timezone import now


# Create your models here.
class Users(models.Model):
    Login = models.TextField(unique=True)
    Password = models.TextField()
    Email = models.EmailField(unique=True)
    Amount = models.IntegerField(default=0)
    Name = models.TextField()
    Surname = models.TextField()
    Avatar = models.ImageField(upload_to='img/', null=True)


class Statistics(models.Model):
    UserID = models.IntegerField()
    Amount = models.IntegerField()
    Date = models.DateTimeField(default=now, null=True)
    Category = models.TextField()
