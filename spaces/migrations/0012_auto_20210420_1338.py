# Generated by Django 3.2 on 2021-04-20 13:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('spaces', '0011_auto_20210420_1317'),
    ]

    operations = [
        migrations.AlterField(
            model_name='price',
            name='unit_type',
            field=models.CharField(choices=[('per hour', 'per hour'), ('per day', 'per day'), ('per month', 'per month')], max_length=30),
        ),
        migrations.AlterField(
            model_name='space',
            name='window',
            field=models.CharField(choices=[('yes', 'with window view'), ('no', 'without window view'), ('n/a', 'not applicable')], max_length=30),
        ),
    ]
