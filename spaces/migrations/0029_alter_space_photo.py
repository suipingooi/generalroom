# Generated by Django 3.2.2 on 2021-05-15 15:28

from django.db import migrations
import pyuploadcare.dj.models


class Migration(migrations.Migration):

    dependencies = [
        ('spaces', '0028_alter_price_cost'),
    ]

    operations = [
        migrations.AlterField(
            model_name='space',
            name='photo',
            field=pyuploadcare.dj.models.ImageField(),
        ),
    ]
