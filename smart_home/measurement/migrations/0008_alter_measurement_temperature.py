# Generated by Django 4.2.4 on 2023-08-25 10:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('measurement', '0007_alter_measurement_options_alter_sensor_options_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='measurement',
            name='temperature',
            field=models.FloatField(),
        ),
    ]