# Generated by Django 3.2 on 2021-04-19 05:15

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('spaces', '0004_timeslot_unit_credits'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Timeslot',
        ),
    ]