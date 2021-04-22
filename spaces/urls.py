from django.urls import path
import spaces.views

urlpatterns = [
    path('', spaces.views.index, name='bookspace'),
    path('add', spaces.views.add_space, name='addspace'),
    path('update/<space_id>', spaces.views.update_space, name='updatespace'),
    path('delete/<space_id>', spaces.views.delete_space, name='deletespace'),
    path('price/view', spaces.views.view_pricelist, name='viewpricelist'),
    path('price/add', spaces.views.add_price, name='addprice'),
    path('price/edit/<price_id>', spaces.views.update_price, name='updateprice'),
    path('price/delete/<price_id>', spaces.views.delete_price, name='delprice')
]
