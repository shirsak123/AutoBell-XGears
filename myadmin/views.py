# External Import
from django.shortcuts import render

# Internal Import
from orders.models import Order

def index(request):
    context = {}
    context['segment'] = 'index'
    return render(request,'myadmin/index.html',context)


def orders(request):
    orders_obj = Order.objects.all()
    context = {
        'orders': orders_obj,
    }
    print(orders_obj)
    return render(request,'myadmin/orders.html',context)
