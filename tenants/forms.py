from django import forms
from django.forms import ModelForm
from .models import Client, ViewRequest


class Date(forms.DateInput):
    input_type = 'date'


class Time(forms.TimeInput):
    input_type = 'time'


class ClientForm(ModelForm):
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


class ViewRequestForm(ModelForm):
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
        widgets = {
            'viewing_date': Date(),
            'viewing_time': Time(),
            'preferred_startdate': Date(),
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
