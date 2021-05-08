from django.db import models
from django.contrib.auth.models import User
from spaces.models import Space
# Create your models here.


class Collection(models.Model):
    name = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    space_id = models.ForeignKey(Space, on_delete=models.SET_NULL, null=True)
    quantity = models.IntegerField(blank=False)
    unit_type = models.CharField(blank=False, max_length=255)
    start_date = models.DateField(blank=False)
    start_time = models.TimeField(blank=False)
    payment = models.DecimalField(blank=False, max_digits=6,
                                  decimal_places=2,)

    def __str__(self):
        return (str(self.name) + " paid " + str(self.payment)
                + " for " + str(self.space_id))
