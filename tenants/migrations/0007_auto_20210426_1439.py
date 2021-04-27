# Generated by Django 3.2 on 2021-04-26 14:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tenants', '0006_alter_viewrequest_subject_message'),
    ]

    operations = [
        migrations.AlterField(
            model_name='viewrequest',
            name='preferred_startdate',
            field=models.DateField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='viewrequest',
            name='subject_message',
            field=models.TextField(blank=True, default=0),
            preserve_default=False,
        ),
    ]
