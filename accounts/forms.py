from pyexpat import model
from django import forms
from django.contrib.auth.models import User

class UpdateUser(forms.ModelForm):
    class Meta:
        model=User
        fields=[
            "first_name",
            "last_name",
            "username",
            "email"
        ]