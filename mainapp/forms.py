from dataclasses import field
from email.headerregistry import Group
from pyexpat import model
from django import forms
from django.contrib.auth.models import User
from .models import Group, Message, User_Group

class CreateGroup(forms.ModelForm):
    class Meta:
        model = Group
        fields=[
            "name",
            "description",
            "subject",
            "allow"
        ]

class InsertUserGroup(forms.ModelForm):
    class Meta:
        model = User_Group
        fields=[]

class AddMessage(forms.ModelForm):
    class Meta:
        model = Message
        fields=[
            "description"
        ]