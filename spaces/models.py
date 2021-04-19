from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator

# Create your models here.


class Space(models.Model):
    space_type = models.CharField(blank=False, max_length=255)
    description = models.TextField(blank=False)
    seat_capacity = models.PositiveIntegerField(
        default=1, validators=[MinValueValidator(1), MaxValueValidator(30)])

    def __str__(self):
        return self.space_type
