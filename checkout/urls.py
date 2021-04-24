from django.urls import path

from .views import checkout, pay_success

urlpatterns = [
    path('', checkout, name='checkout'),
    path('payment_completed', pay_success)
]
