from django.shortcuts import (
    render, redirect, reverse, get_object_or_404, HttpResponse)
from django.views.decorators.csrf import csrf_exempt
from django.contrib import messages
from django.contrib.auth.models import User
from .models import Collection
import datetime
from datetime import timedelta
from django.core.mail import send_mail
from TheGeneralRoom.settings import ADMINS

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

        if space['preferred_start_date'] == "":
            messages.error(request, 'You must update a start date')
            return redirect(reverse('basket_view'))

        if space['preferred_start_time'] == "":
            messages.error(request, 'You must update a start time')
            return redirect(reverse('basket_view'))

        line_item = {
            "name": space_model.space_type + ":" + space_model.description,
            "amount": (int(price_model.cost)*int(price_model.min_count))*100,
            "quantity": space['unit'],
            "description": ("(" + str(space['bundle'])
                            + str(space['unit_type'])
                            + "s@SGD" + str(price_model.cost)
                            + "/" + str(space['unit_type'])+")each"
                            + " -- startdate: "
                            + str(space['preferred_start_date'])),
            "currency": "SGD",
        }

        line_items.append(line_item)

        all_ids.append({
            'space_id': space_id,
            'quantity': space['quantity'],
            'unit_type': space['unit_type'],
            'start_date': space['preferred_start_date'],
            'start_time': space['preferred_start_time'],
            'paid': int(price_model.cost)*int(
                price_model.min_count)*int(space['unit']),
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
    request.session['basket'] = {}

    return render(request, 'checkout/checkout-template.html', {
        'session_id': session.id,
        'public_key': settings.STRIPE_PUBLISHABLE_KEY,
    })


@csrf_exempt
def pay_success(request):
    payload = request.body
    sign_header = request.META['HTTP_STRIPE_SIGNATURE']

    event = None

    endpoint_secret = settings.STRIPE_ENDPOINT_SECRET

    try:
        event = stripe.Webhook.construct_event(
            payload, sign_header, endpoint_secret
        )
    except ValueError as e:
        messages.error(request, e)
        return HttpResponse(status=400)
    except stripe.error.SignatureVerificationError as e:
        messages.error(request, e)
        return HttpResponse(status=400)

    if event['type'] == 'checkout.session.completed':
        session = event['data']['object']
        all_ids_str = session['metadata']['all_ids']
        all_ids = json.loads(all_ids_str)

        userid = session['client_reference_id']
        userobj = get_object_or_404(User, pk=userid)
        index = len(all_ids)
        order = []

        for item in all_ids:
            index -= 1
            spaceid = all_ids[index]['space_id']
            spaceobj = get_object_or_404(Space, pk=spaceid)

            space = str(spaceobj.space_type)
            startdate = all_ids[index]['start_date']
            starttime = all_ids[index]['start_time']
            itemcost = all_ids[index]['paid']
            itemcount = (str(all_ids[index]['quantity']) +
                         str(all_ids[index]['unit_type']))

# transaction data saved to model
            item = Collection(
                name=userobj,
                space_id=spaceobj,
                quantity=int(all_ids[index]['quantity']),
                unit_type=all_ids[index]['unit_type'],
                start_date=startdate,
                start_time=starttime,
                payment=itemcost,
                timestamp=(datetime.datetime.now() + timedelta(hours=8)),
            )
            item.save()

            orderitem = ('PAID SGD' + str(itemcost) + ' for ' + itemcount
                         + ' ' + space + ' starting ' + startdate
                         + ' at ' + starttime)
            order.append(orderitem)

# email to admin
        amount = session['amount_total']/100
        admin_message = ('Payment amounting to SGD' + str(amount)
                         + ' received from '
                         + str(userobj) + ' for the following:'
                         + '\n'
                         + '\n'.join(order))
        send_mail(
            'Django Admin - Payment Received',
            admin_message,
            'tgrlgbdemo@gmail.com',
            [ADMINS],
            fail_silently=False
        )

# email to client
        recipient = userobj.email
        message = ('Dear ' + str(userobj).capitalize() + ','
                   + '\n'
                   + '\n Thank you for your continuous support.'
                   + '\n We have received the following payments:'
                   + '\n'
                   + '\n Amount:'
                   + '\n SGD' + str(amount)
                   + '\n'
                   + '\n Spaces:'
                   + '\n'
                   + '\n'.join(order)
                   + '\n'
                   + '\n'
                   + '\n TGR Admin')

        send_mail(
            'TGR - Payment Received',
            message,
            'tgrlgbdemo@gmail.com',
            [recipient],
            fail_silently=False
        )

        return HttpResponse(status=200)


def success_endpoint(request):
    request.session['basket'] = {}
    messages.success(request, 'Payment Successful, Thank You for '
                     + 'your order. Receipt will be emailed shortly.')
    return render(request, "main/home-template.html")


def cancel_endpoint(request):
    messages.warning(request, 'Payment Cancelled')
    spaces = Space.objects.all().order_by('-id')
    return render(request, 'spaces/index-template.html', {
        'spaces': spaces
    })


def view_collection(request):
    collection = Collection.objects.all().order_by('-timestamp')

    return render(request, 'checkout/transacted-template.html', {
        'col': collection,
    })
