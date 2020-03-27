from __future__ import unicode_literals
from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth import update_session_auth_hash, login, authenticate, logout as log, login as auth_login


def home(request):
    return render(request, 'register.html')

def signup(request):
    if request.method == "POST":
        name = request.POST['name']
        email = request.POST['email']
        username = request.POST['username']
        password = request.POST['password']
        photo = request.POST['photo']

        u = User.objects.create_user(username, email, password, photo)
        u.save()
        return redirect('/')
    else:
        return render(request, 'register.html')


def signin(request):
    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(username=username, password=password)
        if user is not None:
            if user.is_authenticated:
                auth_login(request, user)
                return render(request, 'register.html')
            else:
                return redirect('register')
        else:
            messages.add_message(request, messages.INFO, 'Username/Password is wrong...!')
            return redirect('register')
    else:
            return render(request, 'login.html')


@login_required(login_url='/login')
def logout(request):
    log(request)
    return redirect('/')