# Generated by Django 3.2 on 2021-05-08 09:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('checkout', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='collection',
            name='start_date',
            field=models.CharField(max_length=30),
        ),
        migrations.AlterField(
            model_name='collection',
            name='start_time',
            field=models.CharField(max_length=30),
        ),
    ]