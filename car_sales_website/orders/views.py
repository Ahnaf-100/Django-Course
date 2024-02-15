from django.shortcuts import render, redirect
from .models import Order
from carlist.models import Car
from django.contrib import messages
from django.views.generic import ListView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required


@method_decorator(login_required, name='dispatch')
def place_order(request, car_id):
    if request.user.is_authenticated:
        car = Car.objects.get(id=car_id)
        if car.quantity > 0:
            Order.objects.create(user=request.user, car=car)
            car.quantity -= 1
            car.save()
            return redirect('homepage')
        else:
            messages.warning(request, 'This product is out of stock')
    return redirect('homepage')

@method_decorator(login_required, name='dispatch')
class OrderHistoryView(LoginRequiredMixin, ListView):
    template_name = 'profile.html'
    context_object_name = 'orders'
    def get_queryset(self):
        return Order.objects.filter(user=self.request.user)