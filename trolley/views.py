from django.shortcuts import render, get_object_or_404, redirect, reverse
from django.contrib import messages

# Create your views here.
from spaces.models import Space, Price


def add_to_trolley(request, space_id):
    trolley = request.session.get('basket', {})
    space = get_object_or_404(Space, pk=space_id)
    priceid = space.price_id
    price = get_object_or_404(Price, pk=priceid)
    min_count = price.min_count

    if min_count > 1:
        qty = min_count
    else:
        qty = 1

    total_cost = qty*float(price.cost)

    if space_id in trolley:
        trolley[space_id]['unit'] += 1
        trolley[space_id]['qty'] += qty
        trolley[space_id]['total'] += float(total_cost)
    else:
        trolley[space_id] = {
            'id': space_id,
            'item': space.description,
            'price': float(price.cost),
            'unit_type': price.unit_type,
            'total': float(total_cost),
            'disclaimer': price.valid_period,
            'bundle': price.min_count,
            'qty': qty,
            'unit': 1,
            'photo': str(space.photo),
        }

    request.session['basket'] = trolley

    messages.info(request, 'Item added into your trolley')
    return redirect(reverse('bookspace'))


def view_trolley(request):
    trolley = request.session.get('basket', {})
    return render(request, 'trolley/basket_view-template.html', {
        'trolley': trolley
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

        trolley[space_id]['unit'] = int(request.POST['unit'])
        trolley[space_id]['qty'] = int(new_unit)*int(bundle)
        trolley[space_id]['total'] = int(new_unit)*int(bundle)*float(price)

        request.session['basket'] = trolley
        messages.success(request, 'Unit Items Updated')

    return redirect(reverse('basket_view'))
