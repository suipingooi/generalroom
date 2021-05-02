from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator
from pyuploadcare.dj.models import ImageField
# Create your models here.

view = (
    ('yes', 'with window view'),
    ('no', 'without window view'),
    ('n/a', 'not applicable'),
)


rates = (
        ('hour', 'per hour'),
        ('day', 'per day'),
        ('month', 'per month'),
)


class Price(models.Model):
    cost = models.DecimalField(max_digits=10, decimal_places=2,
                               blank=False, default=10,
                               validators=[MinValueValidator('0.01')])
    unit_type = models.CharField(blank=False, choices=rates, max_length=30)
    min_count = models.PositiveIntegerField(
        default=1, validators=[MinValueValidator(1), MaxValueValidator(100)])
    valid_period = models.CharField(blank=True, max_length=255)

    def __str__(self):
        if self.min_count > 1:
            total = self.cost*self.min_count
            if self.valid_period != "":
                return ("SGD" + str(total) + " for " + str(self.min_count)
                        + self.unit_type + "s (@ SGD" + str(self.cost)
                        + "/" + self.unit_type + ") *validity:"
                        + self.valid_period)
            else:
                return ("SGD" + str(total) + " for " + str(self.min_count)
                        + self.unit_type + "s (@ SGD" + str(self.cost)
                        + "/" + self.unit_type + ")")
        else:
            return ("SGD" + str(self.cost) + "/" + self.unit_type
                    + " (min " + str(self.min_count) + self.unit_type + ")")


class Space(models.Model):
    space_type = models.CharField(blank=False, max_length=255)
    description = models.TextField(blank=False)
    area_size = models.PositiveIntegerField(
        default=1, validators=[MinValueValidator(1), MaxValueValidator(1000)])
    seat_capacity = models.PositiveIntegerField(
        default=1, validators=[MinValueValidator(0), MaxValueValidator(40)])
    photo = ImageField(blank=True, manual_crop="")
    printing = models.PositiveIntegerField(
        default=0, validators=[MinValueValidator(0), MaxValueValidator(1000)])
    meeting_room = models.PositiveIntegerField(
        default=0, validators=[MinValueValidator(0), MaxValueValidator(10)])
    view = models.CharField(blank=False, choices=view, max_length=30)
    price = models.ForeignKey(Price, on_delete=models.CASCADE)

    def __str__(self):
        return self.space_type
