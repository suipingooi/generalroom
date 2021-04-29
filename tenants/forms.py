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


MON = (
    ('', 'Filter by month...'),
    ('1', 'Jan'),
    ('2', 'Feb'),
    ('3', 'Mar'),
    ('4', 'Apr'),
    ('5', 'May'),
    ('6', 'Jun'),
    ('7', 'Jul'),
    ('8', 'Aug'),
    ('9', 'Sep'),
    ('10', 'Oct'),
    ('11', 'Nov'),
    ('12', 'Dec'),
)


class QForm(forms.Form):
    company = forms.CharField(label="",
                              max_length=120,
                              required=False,
                              widget=forms.TextInput(
                                  attrs={'placeholder':
                                         'Search by Company Name'}))
    date = forms.ChoiceField(label="",
                             required=False,
                             choices=MON,)
