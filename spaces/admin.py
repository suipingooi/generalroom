from django.contrib import admin

# Register your models here.
from .models import Space, Validity

admin.site.register(Space)
admin.site.register(Validity)
