# Generated by Django 3.2.2 on 2021-05-15 06:25

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tenants', '0076_alter_cradmin_timestamp'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cradmin',
            name='remarks',
            field=models.TextField(),
        ),
        migrations.AlterField(
            model_name='cradmin',
            name='timestamp',
            field=models.DateTimeField(default=datetime.datetime(2021, 5, 15, 14, 25, 4, 270730)),
        ),
    ]
