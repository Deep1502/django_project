from django.urls import path
from django.urls.resolvers import URLPattern

from . import views

urlpatterns = [
    path('register', views.register, name='register'),
    path('login', views.login, name='login'),
    path('logout', views.logout, name='logout'),
    path('viewprofile', views.viewprofile, name='viewprofile'),
    path('editprofile', views.editprofile, name='editprofile'),
]