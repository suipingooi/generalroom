# Generated by Django 3.2 on 2021-04-27 11:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tenants', '0012_alter_client_phone'),
    ]

    operations = [
        migrations.AlterField(
            model_name='client',
            name='phone',
            field=models.CharField(max_length=8),
        ),
    ]