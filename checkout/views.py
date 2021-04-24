from django.shortcuts import render, redirect, reverse, get_object_or_404, HttpResponse

# Create your views here.
from django.conf import settings

import stripe
import json

from spaces.models import Space, Price


def checkout(request):
    stripe.api_key = settings.STRIPE_SECRET_KEY

    trolley = request.session.get('basket', {})

    line_items = []

    all_ids = []

    for space_id, space in trolley.items():
        space_model = get_object_or_404(Space, pk=space_id)
        priceid = space_model.price_id
        price_model = get_object_or_404(Price, pk=priceid)

        line_item = {
            "name": space_model.description,
            "amount": (int(price_model.cost)*int(price_model.min_count))*100,
            "quantity": space['unit'],
            "description": ("(" + str(space['bundle'])
                            + str(space['unit_type'])
                            + "s@SGD" + str(price_model.cost)
                            + "/" + str(space['unit_type'])+")each"),
            "currency": "SGD",
        }

        line_items.append(line_item)

        all_ids.append({
            'space_id': space_id,
            'quantity': space['quantity'],
        })
    session = stripe.checkout.Session.create(
        payment_method_types=['card'],
        line_items=line_items,
        client_reference_id=request.user.id,
        metadata={
            "all_ids": json.dumps(all_ids),
        },
        mode="payment",
        success_url=settings.STRIPE_SUCCESS_URL,
        cancel_url=settings.STRIPE_CANCEL_URL,
    )
    return render(request, 'checkout/checkout-template.html', {
        'session_id': session.id,
        'public_key': settings.STRIPE_PUBLISHABLE_KEY,
    })
