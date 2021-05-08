# Generated by Django 3.2 on 2021-05-07 02:06

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('trolley', '0002_auto_20210507_0203'),
    ]

    operations = [
        migrations.RenameField(
            model_name='timeslot',
            old_name='preferred_end',
            new_name='preferred_start_date',
        ),
        migrations.RemoveField(
            model_name='timeslot',
            name='preferred_start',
        ),
        migrations.AddField(
            model_name='timeslot',
            name='preferred_start_time',
            field=models.TimeField(default=django.utils.timezone.now),
            preserve_default=False,
        ),
    ]