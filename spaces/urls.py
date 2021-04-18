from django.urls import path
import spaces.views

urlpatterns = [
    path('', spaces.views.index, name='bookspace'),
    path('add', spaces.views.add_space, name='addspace'),
    path('update/<space_id>', spaces.views.update_space, name='updatespace'),
    path('delete/<space_id>', spaces.views.delete_space, name='deletespace')
]
