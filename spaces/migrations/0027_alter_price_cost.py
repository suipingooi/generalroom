# Generated by Django 3.2 on 2021-05-02 14:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('spaces', '0026_alter_space_price'),
    ]

    operations = [
        migrations.AlterField(
            model_name='price',
            name='cost',
            field=models.PositiveIntegerField(default=10),
        ),
    ]
