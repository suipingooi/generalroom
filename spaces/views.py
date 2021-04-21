from django.shortcuts import render, reverse, redirect, get_object_or_404
from .models import Space, Price
from .forms import SpaceForm, PriceForm
from django.contrib import messages

# Create your views here.


def index(request):
    spaces = Space.objects.all()
    return render(request, "spaces/index-template.html", {
        'spaces': spaces
    })

# spaces for booking


def add_space(request):
    if request.method == 'POST':
        space_form = SpaceForm(request.POST)
        if space_form.is_valid():
            space_form.save()
            messages.success(request, 'New Space Added')
            return redirect(reverse(index))
        pass
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
            return redirect(reverse(index))
        else:
            return render(request, 'spaces/space_update-template.html', {
                'form': space_form,
                'space': space_to_update
            })
    else:
        space_form = SpaceForm(instance=space_to_update)
        return render(request, 'spaces/space_update-template.html', {
            'form': space_form,
            'space': space_to_update
        })


def delete_space(request, space_id):
    space_to_delete = get_object_or_404(Space, pk=space_id)
    if request.method == "POST":
        space_to_delete.delete()
        return redirect(index)
    else:
        return render(request, 'spaces/space_delete-template.html', {
            'space': space_to_delete
        })


# CRUD pricelist
def add_price_list(request):
    if request.method == 'POST':
        pricelist_form = PriceForm(request.POST)
        if pricelist_form.is_valid():
            pricelist_form.save()
            messages.success(request, 'New Entry Added to Price List')
            return redirect(reverse(index))
        pass
    else:
        pricelist_form = PriceForm()
        return render(request, 'spaces/price_add-template.html', {
            'form': pricelist_form
        })

# validity / timeslots of booking
