# Generated by Django 3.2 on 2021-04-20 13:17

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('spaces', '0010_alter_space_monthly_print_credits'),
    ]

    operations = [
        migrations.CreateModel(
            name='Price',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cost', models.PositiveIntegerField(default=1, validators=[django.core.validators.MinValueValidator(1), django.core.validators.MaxValueValidator(6000)])),
                ('unit_type', models.CharField(choices=[('hour', 'per_hour'), ('day', 'per_day'), ('month', 'per_month')], max_length=30)),
                ('unit_count', models.PositiveIntegerField(blank=True, null=True)),
            ],
        ),
        migrations.RenameField(
            model_name='space',
            old_name='monthly_meeting_room_credits',
            new_name='monthly_meeting_room_credit_hour',
        ),
        migrations.RenameField(
            model_name='space',
            old_name='monthly_print_credits',
            new_name='monthly_print_credit_page',
        ),
        migrations.RemoveField(
            model_name='space',
            name='price_per_hour',
        ),
        migrations.AddField(
            model_name='space',
            name='area_size',
            field=models.PositiveIntegerField(default=1, validators=[django.core.validators.MinValueValidator(1), django.core.validators.MaxValueValidator(1000)]),
        ),
        migrations.AddField(
            model_name='space',
            name='window',
            field=models.CharField(choices=[('yes', 'with window view'), ('no', 'without window view')], default=1, max_length=30),
            preserve_default=False,
        ),
    ]
