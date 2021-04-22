# Generated by Django 3.2 on 2021-04-19 11:31

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('spaces', '0007_auto_20210419_0704'),
    ]

    operations = [
        migrations.AddField(
            model_name='space',
            name='mth_meetroom_credits',
            field=models.PositiveIntegerField(default=0, validators=[django.core.validators.MinValueValidator(0), django.core.validators.MaxValueValidator(4)]),
        ),
        migrations.AddField(
            model_name='space',
            name='mth_print_credits',
            field=models.PositiveIntegerField(default=30, validators=[django.core.validators.MinValueValidator(1), django.core.validators.MaxValueValidator(60)]),
        ),
        migrations.AddField(
            model_name='space',
            name='price_per_hour',
            field=models.PositiveIntegerField(default=10, validators=[django.core.validators.MinValueValidator(1), django.core.validators.MaxValueValidator(6000)]),
        ),
    ]