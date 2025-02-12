from django.shortcuts import render
from django.views.generic import ListView

from .models import *


class CarView(ListView):
    model = CarsModel
    template_name = 'shop/index.html'
    extra_context = {
        'title': "Namangan Avto",
    }
    context_object_name = 'cars'






def about(requests):
    return render(requests, 'shop/about.html')


def booking(requests):
    return render(requests, 'shop/booking.html')


def service(requests):
    return render(requests, 'shop/service.html')


def detail(requests):
    return render(requests, 'shop/detail.html')


def contact(requests):
    return render(requests, 'shop/contact.html')

