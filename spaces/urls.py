from django.urls import path
import spaces.views

urlpatterns = [
    path('', spaces.views.index, name='bookspace'),
    path('add', spaces.views.add_space),
]
