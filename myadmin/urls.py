from django.urls import path
from . import views

urlpatterns = [
    path('',views.index, name="dashboard"),
    path('orders/',views.orders, name="orders"),
]

app_name = "myadmin"

