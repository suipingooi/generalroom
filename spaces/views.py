from django.shortcuts import render, reverse, redirect, get_object_or_404
from .models import Space
from .forms import SpaceForm
from django.contrib import messages

# Create your views here.


def index(request):
    spaces = Space.objects.all()
    return render(request, "spaces/index-template.html", {
        'spaces': spaces
    })


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
                'form': space_form
            })
    else:
        space_form = SpaceForm(instance=space_to_update)
        return render(request, 'spaces/space_update-template.html', {
            'form': space_form
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
