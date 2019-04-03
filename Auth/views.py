from django.shortcuts import render, redirect, reverse
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import authenticate, login as auth_login

# Create your views here.
def signup(request):
    if request.method == 'GET':
        return render(request, 'Auth/signup.html')
    
    if request.method == 'POST':
        if User.objects.filter(username=request.POST.get('user_email')).count() > 0:
            messages.error(request, 'USER ALREADY EXISTS')
            return HttpResponseRedirect(reverse('Auth:signup'))
        else:
            obj_user = User()
            obj_user.username = request.POST.get('user_email')
            obj_user.first_name = request.POST.get('user_first_name')
            obj_user.last_name = request.POST.get('user_last_name')
            obj_user.set_password(request.POST.get('user_password'))
            obj_user.save()

            messages.success(request, 'USER CREATED SUCCESSFULLY')
            return HttpResponseRedirect(reverse('Auth:login'))

def login(request):
    if request.method == 'GET':
        if request.user.is_authenticated():
            return HttpResponseRedirect(reverse('Schedule:dashboard'))
        return render(request, 'Auth/login.html')
    
    if request.method == 'POST':
        if User.objects.filter(username=request.POST.get('user_email')).count() == 0:
            messages.error(request, "USER DOESN'T EXIST")
            return HttpResponseRedirect(reverse('Auth:login'))
        else:
            obj_user = User()
            username = request.POST.get('user_email')
            password = request.POST.get('user_password')
            obj_user = authenticate(username=username, password=password)
            if obj_user is not None:
                auth_login(request, obj_user)
                messages.success(request, 'LOGIN SUCCESSFULL')
                return HttpResponseRedirect(reverse('Schedule:dashboard'))
            else:
                messages.error(request, 'INVALID CREDENTIALS')
                return HttpResponseRedirect(reverse('Auth:login'))

            messages.error(request, 'SOME ERROR OCCURRED WHILE LOGIN')
            return HttpResponseRedirect(reverse('Auth:login'))