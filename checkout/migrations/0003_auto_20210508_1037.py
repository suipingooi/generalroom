# Generated by Django 3.2 on 2021-05-08 10:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('checkout', '0002_auto_20210508_0911'),
    ]

    operations = [
        migrations.AddField(
            model_name='collection',
            name='unit_type',
            field=models.CharField(default=1, max_length=255),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='collection',
            name='start_date',
            field=models.DateField(),
        ),
        migrations.AlterField(
            model_name='collection',
            name='start_time',
            field=models.TimeField(),
        ),
    ]
