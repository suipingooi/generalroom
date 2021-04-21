from django import forms
from .models import Space, Validity, Price


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


class ValidityForm(forms.ModelForm):
    class Meta:
        model = Validity
        fields = {
            'count_credit',
            'start_datetime',
            'end_datetime',
        }


class PriceForm(forms.ModelForm):
    class Meta:
        model = Price
        fields = {
            'cost',
            'unit_type',
            'min_count',
        }
