from django.shortcuts import render
from store.models import Product

def home(request):
    products = Product.objects.all().filter(is_available=True)
    latest = Product.objects.all().filter(is_available=True).order_by('created_date')[:6]

    context = {
        'products': products,
        'latest': latest
    }
    return render(request, 'home.html', context)
