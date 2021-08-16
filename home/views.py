from django.shortcuts import render, redirect

# Create your views here.

def home(request):
    return render(request,'home/index.html')

def aboutUs(request):
    return render(request,'home/about-us.html')

def contactUs(request):
    return render(request,'home/contact-us.html')