# Generated by Django 3.2 on 2021-04-19 04:55

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('spaces', '0003_timeslot'),
    ]

    operations = [
        migrations.AddField(
            model_name='timeslot',
            name='unit_credits',
            field=models.PositiveIntegerField(default=1, validators=[django.core.validators.MinValueValidator(1), django.core.validators.MaxValueValidator(90)]),
        ),
    ]
