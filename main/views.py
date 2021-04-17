from django.shortcuts import render

# Create your views here.


def index(request):
    return render(request, "main/home-template.html")


def aboutus(request):
    return render(request, "main/aboutus-template.html")


def vtour(request):
    return render(request, "main/vtour-template.html")
