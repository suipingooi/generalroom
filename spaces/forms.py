from django import forms
from .models import Space, Validity


class SpaceForm(forms.ModelForm):
    class Meta:
        model = Space
        fields = {
            'space_type',
            'description',
            'seat_capacity',
            'price_per_hour',
            'monthly_print_credits',
            'monthly_meeting_room_credits'
        }


class ValidityForm(forms.ModelForm):
    class Meta:
        model = Validity
        fields = {'unit_credits', 'start', 'end', }
