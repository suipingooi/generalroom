from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator

# Create your models here.


class Validity(models.Model):
    count_credit = models.PositiveIntegerField(
        default=1, validators=[MinValueValidator(1), MaxValueValidator(90)])
    start_datetime = models.DateTimeField(blank=False)
    end_datetime = models.DateTimeField(blank=False)

    def __str__(self):
        return ("START: " + self.start_datetime + " END: " + self.end_datetime)


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
    cost = models.PositiveIntegerField(
        default=10, validators=[MinValueValidator(1), MaxValueValidator(6000)])
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
                        + "/" + self.unit_type + ") *validity:" + self.valid_period)
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
        default=1, validators=[MinValueValidator(1), MaxValueValidator(30)])
    monthly_print_credit_page = models.PositiveIntegerField(
        default=30, validators=[MinValueValidator(0), MaxValueValidator(60)])
    monthly_meeting_room_credit_hour = models.PositiveIntegerField(
        default=0, validators=[MinValueValidator(0), MaxValueValidator(4)])
    window = models.CharField(blank=False, choices=view, max_length=30)
    price = models.ForeignKey(Price, on_delete=models.CASCADE)

    def __str__(self):
        return self.space_type
