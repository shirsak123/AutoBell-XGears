from django.shortcuts import render
from store.models import Product

#Sorting Method/Function
def getavg(obj):
    return obj.averageReview()

def home(request):
    qs = Product.objects.filter()
    sale = qs[:6]
    latest = Product.objects.all().filter(is_available=True).order_by('created_date')[:6]
    mostPopular = sorted(qs,key=getavg,reverse=True)[:6]

    context = {
        'products': sale,
        'latest': latest,
        'mostPopular': mostPopular
    }
    return render(request, 'home.html', context)
