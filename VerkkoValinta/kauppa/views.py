from django.shortcuts import render, redirect
from  .models import *
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .forms import *
from django import forms

# Create your views here.
def home(request):
  random_products = Product.objects.order_by('?')[:8]
  context ={'random_products': random_products}
  return render(request, 'home.html', context)

def about(request):
  return render(request, 'about.html')

def login_user(request):
  if request.method == 'POST':
    username = request.POST['username']
    password = request.POST['password']
    user = authenticate(request, username=username, password=password)
    if user is not None:
      login(request, user)
      messages.success(request, 'You are now logged in')
      return redirect('home')
    else:
      messages.error(request, 'Invalid credentials')
  else:
    return render(request, 'login.html')

def logout_user(request):
  logout(request)
  messages.success(request, 'You have been logged out')
  return redirect('home')

def register_user(request):
	form = SignUpForm()
	if request.method == "POST":
		form = SignUpForm(request.POST)
		if form.is_valid():
			form.save()
			username = form.cleaned_data['username']
			password = form.cleaned_data['password1']
			# log in user
			user = authenticate(username=username, password=password)
			login(request, user)
			messages.success(request, ("Username Created - Please Fill Out Your User Info Below..."))
			return redirect('update_info')
		else:
			messages.success(request, ("Whoops! There was a problem Registering, please try again..."))
			return redirect('register')
	else:
		return render(request, 'register.html', {'form':form})