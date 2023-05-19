from http.client import HTTPResponse
from django.shortcuts import render, redirect
from django.contrib.auth.models import User, auth
from django.contrib import messages
from django.http import HttpResponseRedirect

from accounts.forms import UpdateUser

# Create your views here.
def register(request):
    if request.method=="POST":
        first_name=request.POST['first_name']
        last_name=request.POST['last_name']
        username=request.POST['username']
        email=request.POST['email']
        password=request.POST['password1']
        confirm_password=request.POST['password2']
        message=""
        if password==confirm_password:
            if User.objects.filter(username=username).exists():
                message=message+'Username already exists!  '
            elif User.objects.filter(email=email).exists():
                message=message+'Email already exists!  '
            else:
                user=User.objects.create_user(username=username, password=password, email=email, first_name=first_name, last_name=last_name)
                user.save()
                message=message+'You are registered successfully!  '
                return redirect('login')
        else:
            message=message+'Passwords are not matching!  '
        messages.info(request, message)
        return redirect('register')
    else:
        return render(request, 'register.html')

def login(request):
    if request.method=='POST':
        username=request.POST['username']
        password=request.POST['password']

        user = auth.authenticate(username=username, password=password)
        if user is not None:
            auth.login(request, user)
            return redirect('/')
        else:
            messages.info(request, 'Invalid credentials!!')
            return redirect('login')
    else:
        return render(request, 'login.html')

def logout(request):
    auth.logout(request)
    return redirect('/')

def viewprofile(request):
    currentuser=request.user
    return render(request, 'viewprofile.html', {'user':currentuser})

def editprofile(request):
    context={}
    user=request.user
    form=UpdateUser(request.POST, instance=user)
    if form.is_valid():
        form.save()
        return HttpResponseRedirect("viewprofile")
    context["form"]=form
    return render(request, "editprofile.html", context)