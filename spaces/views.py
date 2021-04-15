from django.shortcuts import render
from .models import Space

# Create your views here.


def index(request):
    spaces = Space.objects.all()
    return render(request, "spaces/index-template.html", {
        'spaces': spaces
    })

