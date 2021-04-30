from django import forms
from .models import Space, Price


class SpaceForm(forms.ModelForm):
    class Meta:
        model = Space
        fields = {
            'space_type',
            'description',
            'area_size',
            'seat_capacity',
            'printing',
            'meeting_room',
            'view',
            'price',
            'photo',
        }
    field_order = [
        'space_type',
        'description',
        'seat_capacity',
        'photo',
        'price',
        'area_size',
        'printing',
        'meeting_room',
        'view',
    ]


class PriceForm(forms.ModelForm):
    class Meta:
        model = Price
        fields = {
            'cost',
            'unit_type',
            'min_count',
            'valid_period',
        }
    field_order = [
        'cost',
        'unit_type',
        'min_count',
        'valid_period',
    ]
