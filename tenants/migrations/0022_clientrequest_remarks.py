# Generated by Django 3.2 on 2021-05-02 00:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tenants', '0021_remove_clientrequest_remarks'),
    ]

    operations = [
        migrations.AddField(
            model_name='clientrequest',
            name='remarks',
            field=models.TextField(blank=True),
        ),
    ]