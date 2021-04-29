from django.db import models
from django.core.validators import (
    MaxValueValidator, MinValueValidator, RegexValidator)
import datetime
from datetime import timedelta
from django import forms
# Create your models here.


def valiDate(date):
    if date < datetime.date.today():
        raise forms.ValidationError(
            "The date cannot be in the past!")
    elif date <= datetime.date.today() + timedelta(hours=48):
        raise forms.ValidationError(
            "Please give us 48hrs advance notice!")
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


class ClientRequest(models.Model):
    first_name = models.CharField(blank=False, max_length=255)
    last_name = models.CharField(blank=False, max_length=255)
    email = models.EmailField(blank=False, max_length=320)
    phone = models.CharField(blank=False, max_length=8)
    viewing_date = models.DateField(blank=False, validators=[valiDate])
    viewing_time = models.TimeField(blank=False, validators=[valiTime])
    company_name = models.CharField(blank=False, max_length=320)
    company_size = models.PositiveIntegerField(
        default=1, validators=[MinValueValidator(1), MaxValueValidator(100)])
    space_needed = models.CharField(blank=False, max_length=320)
    preferred_startdate = models.DateField(blank=True, null=True)
    subject_message = models.TextField(blank=True)

    def __str__(self):
        return (self.company_name + " " + self.first_name
                + " " + self.last_name + " " + self.email)
