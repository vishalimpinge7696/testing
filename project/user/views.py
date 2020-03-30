from __future__ import unicode_literals
from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth import update_session_auth_hash, login, authenticate, logout as log, login as auth_login
from .forms import SignupForm
import stripe

stripe.api_key = 'sk_test_uWYsVHakqbXSWexgxfIdA3qM00NhGb6G2X'

def home(request):
    return render(request, 'register.html')

def signup(request):
    if request.method == 'POST':
        form = SignupForm(request.POST, request.FILES)
        if form.is_valid():
            # name = form.cleaned_data['name']
            # photo = form.cleaned_data['photo']
            # email = form.cleaned_data['email']
            # username = form.cleaned_data['username']
            # password = form.cleaned_data['password']
            # contact = form.cleaned_data['contact']
            # User.objects.create_user(name=name, photo=photo, email=email, username=username, password=password, contact=contact)
            fs = form.save(commit=False)
            fs.save()

            return redirect('/')
    else:
           form = SignupForm()
    return render(request, 'register.html', {'form': form})


def signin(request):

    if request.method == 'POST':
          username = request.POST.get('username')
          password = request.POST.get('password')
          user = authenticate(request, username=username, password=password)
          if user:
              auth_login(request, user)
              return redirect('home')
          else:
              messages.add_message(request, messages.INFO, 'The username and/or password you specified are not correct.')
              return redirect('signup')
    else:
         return render(request, 'login.html')


@login_required(login_url='/login')
def logout(request):
    log(request)
    return redirect('/')