# Generated by Django 4.2.4 on 2023-08-21 10:37

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('measurement', '0002_remove_sensor_measurements_measurement_sensor_id'),
    ]

    operations = [
        migrations.RenameField(
            model_name='measurement',
            old_name='sensor_id',
            new_name='sensor',
        ),
    ]
