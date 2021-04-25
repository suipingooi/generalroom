from django.db import models
from django.core.validators import (RegexValidator, MaxValueValidator,
                                    MinValueValidator)

# Create your models here.


class Client(models.Model):
    first_name = models.CharField(blank=False, max_length=255)
    last_name = models.CharField(blank=False, max_length=255)
    email = models.EmailField(blank=False, max_length=320)
    phone = models.IntegerField(blank=False)

    # msg = "Phone must be in (+65)12345678 format"
    # regex = RegexValidator(
    #     regex=r'^(+65)\d{8}$',
    #     message=msg
    # )

    # phone = models.CharField(
    #     validators=[regex], max_length=15, blank=False)

    def __str__(self):
        return (self.first_name + " "
                + self.last_name + " (" + self.email + ") ")


class ViewRequest(models.Model):
    viewing_date = models.DateField(blank=False)
    viewing_time = models.TimeField(blank=False)
    company_name = models.CharField(blank=False, max_length=320)
    company_size = models.PositiveIntegerField(
        default=1, validators=[MinValueValidator(1), MaxValueValidator(100)])
    space_needed = models.CharField(blank=False, max_length=320)
    preferred_startdate = models.DateField(blank=True)
    subject_message = models.TextField(blank=True)

    def __str__(self):
        return (self.company_name + " "
                + str(self.viewing_date) + " " + str(self.viewing_time))
