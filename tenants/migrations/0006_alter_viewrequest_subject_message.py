# Generated by Django 3.2 on 2021-04-26 14:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tenants', '0005_alter_viewrequest_preferred_startdate'),
    ]

    operations = [
        migrations.AlterField(
            model_name='viewrequest',
            name='subject_message',
            field=models.TextField(blank=True, null=True),
        ),
    ]
