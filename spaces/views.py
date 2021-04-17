from django.shortcuts import render, reverse, redirect, get_object_or_404
from .models import Space
from .forms import SpaceForm

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
            return redirect(reverse(index))
        pass
    else:
        space_form = SpaceForm()
        return render(request, 'spaces/addspace-template.html', {
            'form': space_form
        })
