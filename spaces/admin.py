from django.contrib import admin

# Register your models here.
from .models import Space, Price

admin.site.register(Space)
admin.site.register(Price)
