from django.shortcuts import render, reverse, redirect, get_object_or_404
from .models import Space, Price
from .forms import SpaceForm, PriceForm
from django.contrib import messages

# Create your views here.


def bookspace(request):
    spaces = Space.objects.all().order_by('-id')
    return render(request, 'spaces/index-template.html', {
        'spaces': spaces
    })

# spaces for booking


def add_space(request):
    if request.method == 'POST':
        space_form = SpaceForm(request.POST)
        if space_form.is_valid():
            space_form.save()
            messages.success(request, 'New Space Added')
            return redirect(reverse(bookspace))
        else:
            messages.error(
                request, 'Action Unsuccessful, Please check error fields')
            return render(request, 'spaces/space_add-template.html', {
                'form': space_form
            })
    else:
        space_form = SpaceForm()
        return render(request, 'spaces/space_add-template.html', {
            'form': space_form
        })


def update_space(request, space_id):
    space_to_update = get_object_or_404(Space, pk=space_id)
    if request.method == "POST":
        space_form = SpaceForm(request.POST, instance=space_to_update)
        if space_form.is_valid():
            space_form.save()
            messages.success(request, 'Space Entry Updated')
            return redirect(reverse(bookspace))
        else:
            messages.error(
                request, 'Action Unsuccessful, Please check error fields')
            return render(request, 'spaces/space_update-template.html', {
                'form': space_form,
                'space': space_to_update
            })
    else:
        messages.info(request, 'EDIT action will overwrite data')
        space_form = SpaceForm(instance=space_to_update)
        return render(request, 'spaces/space_update-template.html', {
            'form': space_form,
            'space': space_to_update
        })


def delete_space(request, space_id):
    space_to_delete = get_object_or_404(Space, pk=space_id)
    if request.method == "POST":
        space_to_delete.delete()
        messages.success(request, 'Space Entry Deleted')
        return redirect(bookspace)
    else:
        messages.warning(request, 'DELETE action cannot be undone')
        return render(request, 'spaces/space_delete-template.html', {
            'space': space_to_delete
        })


# CRUD pricelist
def view_pricelist(request):
    pricelist = Price.objects.all().order_by('unit_type')
    return render(request, 'spaces/price_view-template.html', {
        'pricelist': pricelist
    })


def add_price(request):
    if request.method == 'POST':
        pricelist_form = PriceForm(request.POST)
        if pricelist_form.is_valid():
            pricelist_form.save()
            messages.success(request, 'New Entry Added to Price List')
            return redirect(reverse(view_pricelist))
        pass
    else:
        pricelist_form = PriceForm()
        return render(request, 'spaces/price_add-template.html', {
            'form': pricelist_form
        })


def update_price(request, price_id):
    price_to_update = get_object_or_404(Price, pk=price_id)
    if request.method == "POST":
        price_form = PriceForm(request.POST, instance=price_to_update)
        if price_form.is_valid():
            price_form.save()
            messages.success(request, 'Price Entry Updated')
            return redirect(reverse(view_pricelist))
        else:
            messages.error(
                request, 'Update Unsuccessful, Please check error fields')
            return render(request, 'spaces/price_update-template.html', {
                'form': price_form,
                'price': price_to_update
            })
    else:
        messages.info(request, 'EDIT action will overwrite data')
        price_form = PriceForm(instance=price_to_update)
        return render(request, 'spaces/price_update-template.html', {
            'form': price_form,
            'price': price_to_update
        })


def delete_price(request, price_id):
    price_to_delete = get_object_or_404(Price, pk=price_id)
    if request.method == "POST":
        price_to_delete.delete()
        messages.success(request, 'Price entry deleted')
        return redirect(view_pricelist)
    else:
        messages.warning(request, 'DELETE action cannot be undone')
        return render(request, 'spaces/price_delete-template.html', {
            'price': price_to_delete
        })

# validity / timeslots for booking
