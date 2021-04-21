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
            'monthly_print_credit_page',
            'monthly_meeting_room_credit_hour',
            'window',
            'price',
        }
    field_order = [
        'space_type',
        'description',
        'seat_capacity',
        'price',
        'area_size',
        'monthly_print_credit_page',
        'monthly_meeting_room_credit_hour',
        'window',
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
