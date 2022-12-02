# Generated by Django 4.1.2 on 2022-11-30 09:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('constructions', '0037_earth_measure_units'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='earth',
            name='measure_units',
        ),
        migrations.RemoveField(
            model_name='earth',
            name='measure_unit',
        ),
        migrations.AddField(
            model_name='earth',
            name='measure_unit',
            field=models.ManyToManyField(blank=True, to='constructions.measureunit'),
        ),
    ]