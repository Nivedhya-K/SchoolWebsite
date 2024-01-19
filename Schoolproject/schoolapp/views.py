from django.shortcuts import render
from django.contrib import messages
from django.shortcuts import render, redirect
from django.contrib.auth.models import User,auth
from django.http import HttpResponse
# Create your views here.
def home(request):
    return render(request,"home.html")
def form(request):
    return render(request,'form.html')
def button(request):
    return render(request,'button.html')
# Create your views here.

