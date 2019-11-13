from django.shortcuts import render
from . import views

def index(request):
    return render(request, 'base.html')

def training(request):
    return render(request, 'training/t_index.html')

def calculator(request):
    return render(request, 'Calculator/bmi.html')