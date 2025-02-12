from django.urls import path

from .views import *



urlpatterns = [
    path('', CarView.as_view(), name='index'),
    path('about/', about, name='about'),
    path('booking/', booking, name='booking'),
    path('service/', service, name='service'),
    path('detail/', detail, name='detail'),
    path('contact/', contact, name='contact'),
]

