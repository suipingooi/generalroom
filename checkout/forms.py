from django import forms
from .models import Collection

class ColForm(forms.ModelForm):
    class Meta:
        model = Collection
        fields = {
            'name',
            'space_id',
            'quantity',
            'start_date',
            'start_time',
            'payment',
        }