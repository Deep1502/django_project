from django.urls import path
from django.urls.resolvers import URLPattern

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('groups', views.viewgroups, name='viewgroups'),
    path('creategroup', views.creategroup, name='creategroup'),
    path('joingroup', views.joingroup, name='joingroup'),
    path('grouppage/<id>', views.grouppage, name='grouppage'),
    path('leave/<id>', views.leave, name='leave'),
    path('newmessage/<id>', views.newmessage, name='newmessage'),
]