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
from orders.models import Order


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
        return True
