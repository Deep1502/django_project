from tokenize import group
from django.shortcuts import render
from datetime import datetime

from .forms import AddMessage, CreateGroup,InsertUserGroup
from .models import Group, Message, User_Group
from django.contrib.auth.models import User
from django.http import HttpResponseRedirect

# Create your views here.
def index(request):
    return render(request, 'index.html')

def viewgroups(request):
    userid=request.user.id
    groups=User_Group.objects.filter(Userid=userid).all()
    return render(request, "groups.html", {'groups': groups})

def creategroup(request):
    context={}
    form=CreateGroup(request.POST)
    if form.is_valid():
        obj=form.save(commit=False)
        obj.ownerid=User.objects.get(pk=request.user.id)
        obj.save()
        groupid=obj.id
        form1 = InsertUserGroup(request.POST)
        obj1= form1.save(commit=False)
        obj1.Userid=User.objects.get(pk=request.user.id)
        obj1.Groupid = Group.objects.get(pk=groupid)
        obj1.save()
        return HttpResponseRedirect("groups")
    context["form"]=form
    return render(request, "creategroup.html", context)

def joingroup(request):
    if request.method=='POST':
        groupid = request.POST['groupid']
        form=InsertUserGroup(request.POST)
        obj=form.save(commit=False)
        obj.Userid=User.objects.get(pk=request.user.id)
        try:
            group=Group.objects.get(pk=groupid)
        except:
            return HttpResponseRedirect("joingroup")
        obj.Groupid=Group.objects.get(pk=groupid)
        obj.save()
        return HttpResponseRedirect("groups")
    else:
        return render(request, "joingroup.html")

def grouppage(request, id):
    group = Group.objects.get(pk=id)
    msg=Message.objects.filter(groupid=id).all()
    return render(request, "grouppage.html",{'group': group,'msg':msg})

def leave(request, id):
    try:
        group = User_Group.objects.get(Groupid=id, Userid=request.user.id)
    except:
        return HttpResponseRedirect("/groups")
    group.delete()
    return HttpResponseRedirect("/groups")

def newmessage(request,id):
    context={}
    form = AddMessage(request.POST)
    if form.is_valid():
        obj=form.save(commit=False)
        obj.userid=User.objects.get(pk=request.user.id)
        obj.groupid=Group.objects.get(pk=id)
        obj.date=datetime.now()
        obj.save()
        url="/grouppage/"+id
        return HttpResponseRedirect(url)
    context["form"]=form
    return render(request, "newmessage.html", context)