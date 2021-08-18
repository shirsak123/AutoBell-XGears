from django.shortcuts import render

# Create your views here.

def index(request):
    context = {}
    context['segment'] = 'index'
    return render(request,'myadmin/index.html',context)
