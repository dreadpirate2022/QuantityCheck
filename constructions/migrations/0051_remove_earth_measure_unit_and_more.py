# Generated by Django 4.1.2 on 2022-12-01 08:03

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('constructions', '0050_remove_earth_measure_unit_dropdown_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='earth',
            name='measure_unit',
        ),
        migrations.AddField(
            model_name='earth',
            name='measure_unit_dropdown',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='constructions.measureunit'),
        ),
    ]
