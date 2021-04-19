from django import forms
from .models import Space


class SpaceForm(forms.ModelForm):
    class Meta:
        model = Space
        fields = {'space_type', 'description', 'seat_capacity'}
