from django.urls import path
import tenants.views

urlpatterns = [
    path('', tenants.views.client_list, name='clientlist'),
    path('add/', tenants.views.add_client, name='add_client'),
    path('update/<tenant_id>', tenants.views.edit_client, name='edit_client'),
    path('delete/<tenant_id>', tenants.views.delete_client,
         name='delete_client'),
]
