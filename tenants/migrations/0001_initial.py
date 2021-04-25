# Generated by Django 3.2 on 2021-04-24 14:26

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Client',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=255)),
                ('last_name', models.CharField(max_length=255)),
                ('email', models.EmailField(max_length=320)),
                ('phone', models.CharField(max_length=15, validators=[django.core.validators.RegexValidator(message='Phone must be in (+65)12345678 format', regex='^(+65)\\d{8}$')])),
            ],
        ),
        migrations.CreateModel(
            name='ViewRequest',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('viewing_date', models.DateField()),
                ('viewing_time', models.TimeField()),
                ('company_name', models.CharField(max_length=320)),
                ('company_size', models.PositiveIntegerField(default=1, validators=[django.core.validators.MinValueValidator(1), django.core.validators.MaxValueValidator(100)])),
                ('space_needed', models.CharField(max_length=320)),
                ('preferred_startdate', models.DateTimeField()),
                ('subject_message', models.TextField()),
            ],
        ),
    ]