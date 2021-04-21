from django.contrib import admin

# Register your models here.
from .models import Space, Validity, Price

admin.site.register(Space)
admin.site.register(Validity)
admin.site.register(Price)
