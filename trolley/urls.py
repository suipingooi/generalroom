from django.urls import path
import trolley.views

urlpatterns = [

    path('', trolley.views.view_trolley, name='basket_view'),
    path('add/<space_id>', trolley.views.add_to_trolley, name='basket_add'),
    path('delete/<space_id>', trolley.views.del_from_trolley,
         name='basket_del'),
    path('update/<space_id>', trolley.views.update_trolley,
         name='basket_update'),
]
