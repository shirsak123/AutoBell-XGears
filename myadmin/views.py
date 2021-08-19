# External Import
from django.shortcuts import render
from django.views.generic import (
    ListView,
    DetailView,
    CreateView,
    UpdateView,
    DeleteView
)
from django.shortcuts import render, redirect
from django.contrib.auth.mixins import (
    LoginRequiredMixin,
    UserPassesTestMixin
)

# Internal Import
from orders.models import Order, OrderProduct


def index(request):
    context = {}
    context['segment'] = 'index'
    return render(request, 'myadmin/index.html', context)


class OrderListView(UserPassesTestMixin, ListView):
    template_name = "myadmin/orders.html"
    model = Order

    # Check if the user can access this page
    # Declare permission who can access this page
    def test_func(self):
        if self.request.user.is_authenticated:
            return self.request.user.is_staff
        return False


class OrderDetailView(UserPassesTestMixin, DetailView):
    queryset = Order.objects.all()
    template_name = "myadmin/order-detail.html"
    pk_url_kwarg = 'pk'

    # Check if the user can access this page
    # Declare permission who can access this page
    def test_func(self):
        if self.request.user.is_authenticated:
            return self.request.user.is_staff
        return False

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        orderId = self.kwargs['pk']
        orderProduct = OrderProduct.objects.all()
        print(orderProduct)
        context["orderProduct"] = orderProduct
        return context


def marked_as_delivered(request, id):
    order = Order.objects.get(id=id)
    order.status = 'Delivered'
    order.save()
    return redirect('myadmin:order-detail', pk=id)


def marked_as_inprogress(request, id):
    order = Order.objects.get(id=id)
    order.status = 'In Progress'
    order.save()
    return redirect('myadmin:order-detail', pk=id)
