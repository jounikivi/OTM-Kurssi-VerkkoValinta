from django.shortcuts import render, redirect
from  .models import *
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages

# Create your views here.
def home(request):
  return render(request, 'home.html')

def about(request):
  return render(request, 'about.html')

def login_user(request):
  return render(request, 'login.html')

def logout_user(request):
  pass
