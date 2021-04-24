from django.contrib import admin

# Register your models here.
from .models import Client, ViewRequest

admin.site.register(Client)
admin.site.register(ViewRequest)

