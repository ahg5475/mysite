from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth import login



def index(request):
    return render(request, 'base.html')

def training(request):
    return render(request, 'training/t_index.html')

def calculator(request):
    return render(request, 'calculator/bmi.html')