from django.urls import path

from .views import (checkout, pay_success, view_collection,
                    success_endpoint, cancel_endpoint)

urlpatterns = [
    path('', checkout, name='checkout'),
    path('payment_completed', pay_success),
    path('transacted', view_collection, name='transacted'),
    path('success', success_endpoint, name='success'),
    path('cancel', cancel_endpoint, name='cancel'),
]
