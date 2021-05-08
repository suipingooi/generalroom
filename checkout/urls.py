from django.urls import path

from .views import checkout, pay_success, view_collection

urlpatterns = [
    path('', checkout, name='checkout'),
    path('payment_completed', pay_success),
    path('transacted', view_collection, name='transacted'),
]
