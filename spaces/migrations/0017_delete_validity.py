# Generated by Django 3.2 on 2021-04-21 03:33

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('spaces', '0016_price_valid_period'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Validity',
        ),
    ]
