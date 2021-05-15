from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator
import datetime
from datetime import timedelta
from django import forms
from django.contrib.auth.models import User
# Create your models here.


# cleaning / validation functions
def valiPhone(phone):
    if phone.isalpha() or len(phone) != 8:
        raise forms.ValidationError('Please enter a valid phone number')
    return phone


def valiDate(date):
    if date < datetime.date.today():
        raise forms.ValidationError(
            "The date cannot be in the past!")
    elif date <= datetime.date.today() + timedelta(hours=48):
        raise forms.ValidationError(
            "Please give us 48hrs advance notice!")
    elif date.weekday() == 5 or date.weekday() == 6:
        raise forms.ValidationError(
            "Please choose a weekday!")
    return date


def valiTime(time):
    hour = int(time.strftime("%H"))
    tmin = int(time.strftime("%M"))
    if hour < 8 or hour > 17:
        raise forms.ValidationError(
            "Our operational hours are between 9am and 6pm!")
    elif hour == 17 and tmin > 30:
        raise forms.ValidationError(
            "Please give yourself at least 30mins for a pleasant visit!")
    return time


# admin - client-request followup model
class crAdmin(models.Model):
    remarks = models.TextField(blank=False)
    manager = models.ForeignKey(
        User, on_delete=models.SET_NULL, null=True, blank=True)
    timestamp = models.DateTimeField(
        default=(datetime.datetime.now() + timedelta(hours=8)))
    crequest = models.ForeignKey('ClientRequest', on_delete=models.CASCADE)

    def __str__(self):
        return (str(self.timestamp) + ' by ' + str(self.manager)
                + ' | ' + self.remarks)


class ClientRequest(models.Model):
    first_name = models.CharField(blank=False, max_length=255)
    last_name = models.CharField(blank=False, max_length=255)
    email = models.EmailField(blank=False, max_length=320)
    phone = models.CharField(
        blank=False, max_length=8, validators=[valiPhone])
    viewing_date = models.DateField(blank=False, validators=[valiDate])
    viewing_time = models.TimeField(blank=False, validators=[valiTime])
    company_name = models.CharField(blank=False, max_length=320)
    company_size = models.PositiveIntegerField(
        default=1, validators=[MinValueValidator(1), MaxValueValidator(100)])
    space_needed = models.CharField(blank=False, max_length=320)
    preferred_startdate = models.DateField(blank=True, null=True)
    subject_message = models.TextField(blank=True)
    remarks = models.ForeignKey(
        'crAdmin', on_delete=models.SET_NULL, null=True)
    lastflup = models.DateTimeField(blank=True, null=True)

    def __str__(self):
        return (self.company_name + " " + self.first_name
                + " " + self.last_name + " " + self.email)
