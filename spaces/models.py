from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator

# Create your models here.


class Validity(models.Model):
    unit_credits = models.PositiveIntegerField(
        default=1, validators=[MinValueValidator(1), MaxValueValidator(90)])
    start = models.DateTimeField(blank=False)
    end = models.DateTimeField(blank=False)

    def __str__(self):
        return ("START: " + self.start + " END: " + self.end)


class Space(models.Model):
    space_type = models.CharField(blank=False, max_length=255)
    description = models.TextField(blank=False)
    seat_capacity = models.PositiveIntegerField(
        default=1, validators=[MinValueValidator(1), MaxValueValidator(30)])
    price_per_hour = models.PositiveIntegerField(
        default=10, validators=[MinValueValidator(1), MaxValueValidator(6000)])
    monthly_print_credits = models.PositiveIntegerField(
        default=30, validators=[MinValueValidator(0), MaxValueValidator(60)])
    monthly_meeting_room_credits = models.PositiveIntegerField(
        default=0, validators=[MinValueValidator(0), MaxValueValidator(4)])

    def __str__(self):
        return self.space_type
