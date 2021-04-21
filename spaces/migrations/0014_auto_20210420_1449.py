# Generated by Django 3.2 on 2021-04-20 14:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('spaces', '0013_space_price'),
    ]

    operations = [
        migrations.RenameField(
            model_name='price',
            old_name='unit_count',
            new_name='min_count',
        ),
        migrations.RenameField(
            model_name='validity',
            old_name='unit_credits',
            new_name='count_credit',
        ),
        migrations.RenameField(
            model_name='validity',
            old_name='end',
            new_name='end_datetime',
        ),
        migrations.RenameField(
            model_name='validity',
            old_name='start',
            new_name='start_datetime',
        ),
        migrations.AlterField(
            model_name='price',
            name='unit_type',
            field=models.CharField(choices=[('per hour', '/hour'), ('per day', '/day'), ('per month', '/month')], max_length=30),
        ),
    ]
