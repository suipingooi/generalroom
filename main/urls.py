from django.urls import path
import main.views

urlpatterns = [
    path('', main.views.index, name='home'),
    path('aboutus', main.views.aboutus, name='aboutus'),
    path('vtour', main.views.vtour, name='vtour'),
]
