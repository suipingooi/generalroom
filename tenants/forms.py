from django import forms
from django.forms import ModelForm
from .models import ClientRequest, crAdmin


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

    # for admin viewing of raw client form submitted to followup
    def __init__(self, *args, **kwargs):
        super(ClientRequestForm, self).__init__(*args, **kwargs)
        instance = getattr(self, 'instance', None)
        if instance and instance.pk:
            self.fields['first_name'].widget.attrs['readonly'] = True
            self.fields['last_name'].widget.attrs['readonly'] = True
            self.fields['email'].widget.attrs['readonly'] = True
            self.fields['phone'].widget.attrs['readonly'] = True
            self.fields['company_name'].widget.attrs['readonly'] = True
            self.fields['company_size'].widget.attrs['readonly'] = True
            self.fields['space_needed'].widget.attrs['readonly'] = True
            self.fields['viewing_date'].widget.attrs['readonly'] = True
            self.fields['viewing_time'].widget.attrs['readonly'] = True
            self.fields['preferred_startdate'].widget.attrs['readonly'] = True
            self.fields['subject_message'].widget.attrs['readonly'] = True


# admin - query form to organize client requests for followup
MONTH = (
    ('', 'Filter by month...'),
    ('1', 'January'),
    ('2', 'February'),
    ('3', 'March'),
    ('4', 'April'),
    ('5', 'May'),
    ('6', 'June'),
    ('7', 'July'),
    ('8', 'August'),
    ('9', 'September'),
    ('10', 'October'),
    ('11', 'November'),
    ('12', 'December'),
)


class QForm(forms.Form):
    name = forms.CharField(label="",
                           max_length=120,
                           required=False,
                           widget=forms.TextInput(
                               attrs={'placeholder':
                                      'Search by Name'}))
    company = forms.CharField(label="",
                              max_length=120,
                              required=False,
                              widget=forms.TextInput(
                                  attrs={'placeholder':
                                         'Search by Company'}))
    date = forms.ChoiceField(label="",
                             required=False,
                             choices=MONTH,)


# admin - form for followup updates to client requests
class AdminForm(ModelForm):
    class Meta:
        model = crAdmin
        fields = {
            'remarks',
            'manager',
        }
