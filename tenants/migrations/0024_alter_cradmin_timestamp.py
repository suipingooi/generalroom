# Generated by Django 3.2 on 2021-05-02 08:32

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('tenants', '0023_alter_clientrequest_remarks'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cradmin',
            name='timestamp',
            field=models.DateTimeField(default=datetime.datetime(2021, 5, 2, 8, 32, 5, 483440, tzinfo=utc)),
        ),
    ]