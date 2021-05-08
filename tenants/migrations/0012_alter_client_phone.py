# Generated by Django 3.2 on 2021-04-27 11:26

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tenants', '0011_remove_client_requests'),
    ]

    operations = [
        migrations.AlterField(
            model_name='client',
            name='phone',
            field=models.CharField(max_length=8, validators=[django.core.validators.RegexValidator(message='Phone number can only be in the following format: 12345678', regex='^(d{9,8})$')]),
        ),
    ]