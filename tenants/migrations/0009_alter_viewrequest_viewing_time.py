# Generated by Django 3.2 on 2021-04-27 02:35

from django.db import migrations, models
import tenants.models


class Migration(migrations.Migration):

    dependencies = [
        ('tenants', '0008_alter_viewrequest_viewing_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='viewrequest',
            name='viewing_time',
            field=models.TimeField(validators=[tenants.models.valiTime]),
        ),
    ]
