from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name="dashboard"),
    path('orders/', views.OrderListView.as_view(), name="orders"),
    path('orders/<int:pk>/',
         views.OrderDetailView.as_view(), name='order-detail'),
    path('orders/mark-delievered/<int:id>/',
         views.marked_as_delivered, name="mark-delivered"),
    path('orders/mark-inprogress/<int:id>/',
         views.marked_as_inprogress, name="mark-inprogress"),
]

app_name = "myadmin"
