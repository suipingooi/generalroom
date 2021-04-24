from django import forms
from .models import Client, ViewRequest


class ClientForm(forms.ModelForm):
    class Meta:
        model = Client
        fields = {
            'first_name',
            'last_name',
            'email',
            'phone',
        }
    field_order = [
        'first_name',
        'last_name',
        'email',
        'phone',
    ]


class ViewRequestForm(forms.ModelForm):
    class Meta:
        model = ViewRequest
        fields = {
            'viewing_date',
            'viewing_time',
            'company_name',
            'company_size',
            'space_needed',
            'preferred_startdate',
            'subject_message',
        }
    field_order = [
        'company_name',
        'company_size',
        'space_needed',
        'viewing_date',
        'viewing_time',
        'preferred_startdate',
        'subject_message',
    ]
