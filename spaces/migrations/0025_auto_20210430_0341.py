# Generated by Django 3.2 on 2021-04-30 03:41

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('spaces', '0024_alter_price_cost'),
    ]

    operations = [
        migrations.RenameField(
            model_name='space',
            old_name='monthly_meeting_room_credit_hour',
            new_name='meeting_room',
        ),
        migrations.RenameField(
            model_name='space',
            old_name='monthly_print_credit_page',
            new_name='printing',
        ),
        migrations.RenameField(
            model_name='space',
            old_name='window',
            new_name='view',
        ),
    ]