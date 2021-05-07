from django.shortcuts import render, get_object_or_404, redirect, reverse
from django.contrib import messages
import datetime
from datetime import timedelta
# Create your views here.
from spaces.models import Space, Price


def add_to_trolley(request, space_id):
    trolley = request.session.get('basket', {})
    space = get_object_or_404(Space, pk=space_id)
    priceid = space.price_id
    price = get_object_or_404(Price, pk=priceid)
    min_count = price.min_count

    if price.valid_period != "":
        disclaimer = "*" + price.valid_period
    else:
        disclaimer = ""

    if min_count > 1:
        qty = min_count
    else:
        qty = 1

    total_cost = qty*float(price.cost)

    if space_id in trolley:
        trolley[space_id]['unit'] += 1
        trolley[space_id]['quantity'] += qty
        trolley[space_id]['total'] += float(total_cost)
    else:
        trolley[space_id] = {
            'id': space_id,
            'item': space.space_type + " | " + space.description,
            'price': float(price.cost),
            'unit_type': price.unit_type,
            'total': float(total_cost),
            'disclaimer': disclaimer,
            'bundle': price.min_count,
            'quantity': qty,
            'unit': 1,
            'photo': str(space.photo),
            'preferred_start_date': "",
            'preferred_start_time': "",
        }

    request.session['basket'] = trolley

    messages.info(request, 'Item added into your trolley')
    return redirect(reverse('bookspace'))


def view_trolley(request):
    trolley = request.session.get('basket', {})
    return render(request, 'trolley/basket_view-template.html', {
        'trolley': trolley,
    })


def del_from_trolley(request, space_id):
    trolley = request.session.get('basket', {})

    if space_id in trolley:
        del trolley[space_id]
        request.session['basket'] = trolley
        messages.info(request, 'Item removed from your trolley')
    return redirect(reverse('basket_view'))


def update_trolley(request, space_id):
    trolley = request.session.get('basket', {})
    if space_id in trolley:
        bundle = trolley[space_id]['bundle']
        price = trolley[space_id]['price']
        new_unit = request.POST['unit']
        start_date = request.POST['preferred_start_date']
        start_time = request.POST['preferred_start_time']

        date = datetime.datetime.strptime(start_date, '%Y-%m-%d')
        print(date)
        if date < datetime.datetime.today():
            messages.error(request, 'The date cannnot be in the past!')
            return redirect(reverse('basket_view'))
        elif date <= datetime.datetime.today() + timedelta(hours=24):
            messages.error(request, 'Please give us at least 48hours notice!')
            return redirect(reverse('basket_view'))

        trolley[space_id]['unit'] = int(request.POST['unit'])
        trolley[space_id]['quantity'] = int(new_unit)*int(bundle)
        trolley[space_id]['total'] = int(new_unit)*int(bundle)*float(price)
        trolley[space_id]['preferred_start_date'] = start_date
        trolley[space_id]['preferred_start_time'] = start_time

        if trolley[space_id]['unit'] == 0:
            del trolley[space_id]
            request.session['basket'] = trolley
            messages.info(request, 'Item removed from your trolley')
            return redirect(reverse('basket_view'))

        request.session['basket'] = trolley
        messages.success(request, 'Item Details Updated')

    return redirect(reverse('basket_view'))
