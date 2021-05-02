from django.contrib import admin

# Register your models here.
from .models import ClientRequest, crAdmin

admin.site.register(ClientRequest)
admin.site.register(crAdmin)
