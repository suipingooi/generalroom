from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator

# Create your models here.


class Space(models.Model):
    nametype = models.CharField(blank=False, max_length=255)
    desc = desc = models.TextField(blank=False)
    seats = models.PositiveIntegerField(
        default=1, validators=[MinValueValidator(1), MaxValueValidator(30)])

    def __str__(self):
        return self.nametype
