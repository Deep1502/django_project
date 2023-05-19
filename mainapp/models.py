import string
from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Group(models.Model):
    name = models.CharField(max_length=100)
    description = models.CharField(max_length=255)
    subject = models.CharField(max_length=100)
    ownerid = models.ForeignKey(User, on_delete=models.DO_NOTHING)
    allow = models.BooleanField(default=False)

class User_Group(models.Model):
    Userid = models.ForeignKey(User, on_delete=models.DO_NOTHING)
    Groupid = models.ForeignKey(Group, on_delete=models.DO_NOTHING)

class Message(models.Model):
    description = models.CharField(max_length=255)
    date = models.DateField()
    groupid = models.ForeignKey(Group, on_delete=models.DO_NOTHING)
    userid = models.ForeignKey(User, on_delete=models.DO_NOTHING)