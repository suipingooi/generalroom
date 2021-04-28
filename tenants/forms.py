from django import forms
from django.forms import ModelForm
from .models import ClientRequest


class Date(forms.DateInput):
    input_type = 'date'


class Time(forms.TimeInput):
    input_type = 'time'


class ClientRequestForm(ModelForm):
    class Meta:
        model = ClientRequest
        fields = {
            'first_name',
            'last_name',
            'email',
            'phone',
            'viewing_date',
            'viewing_time',
            'company_name',
            'company_size',
            'space_needed',
            'preferred_startdate',
            'subject_message',
        }
        widgets = {
            'viewing_date': Date(),
            'viewing_time': Time(),
            'preferred_startdate': Date(),
        }
    field_order = [
        'first_name',
        'last_name',
        'email',
        'phone',
        'company_name',
        'company_size',
        'space_needed',
        'viewing_date',
        'viewing_time',
        'preferred_startdate',
        'subject_message',
    ]
