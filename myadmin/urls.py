from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name="dashboard"),
    path('orders/', views.OrderListView.as_view(), name="orders"),
]

app_name = "myadmin"
