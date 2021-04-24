# Generated by Django 3.2 on 2021-04-23 07:58

import django.core.validators
from django.db import migrations, models
import pyuploadcare.dj.models


class Migration(migrations.Migration):

    dependencies = [
        ('spaces', '0021_alter_space_photo'),
    ]

    operations = [
        migrations.AlterField(
            model_name='price',
            name='cost',
            field=models.DecimalField(decimal_places=3, default=10, max_digits=10, validators=[django.core.validators.MinValueValidator(0), django.core.validators.MaxValueValidator(6000)]),
        ),
        migrations.AlterField(
            model_name='space',
            name='photo',
            field=pyuploadcare.dj.models.ImageField(blank=True),
        ),
    ]