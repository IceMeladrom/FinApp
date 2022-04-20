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
    CostCategory = models.TextField(blank=True)
    CostDescription = models.TextField(blank=True)


class Articles(models.Model):
    Name = models.TextField(editable=True, unique=True)
    Text = models.TextField(editable=True)
    Author = models.TextField()
    AuthorID = models.TextField()
    Created = models.DateTimeField(default=now)
    LastUpdate = models.DateTimeField(editable=True)
    Visits = models.IntegerField(default=0)
    Likes = models.IntegerField(default=0)
    Dislikes = models.IntegerField(default=0)


class Exams(models.Model):
    ArticleID = models.IntegerField()
    Question = models.TextField()
    Answers = models.TextField()
    CorrectAnswer = models.TextField()


class PassedExams(models.Model):
    UserID = models.IntegerField()
    ArticleID = models.IntegerField()
    Result = models.IntegerField()
    MaxResult = models.IntegerField()
    Passed = models.BooleanField()


class ArticlesLikes(models.Model):
    UserID = models.IntegerField()
    ArticleID = models.IntegerField()
    Like = models.BooleanField()


class Purpose(models.Model):
    UserID = models.IntegerField()
    Purpose = models.TextField()
