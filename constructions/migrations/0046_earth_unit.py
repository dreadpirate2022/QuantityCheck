# Generated by Django 4.1.2 on 2022-11-30 19:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('constructions', '0045_measureunit_remove_earth_measure_unit_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='earth',
            name='unit',
            field=models.CharField(blank=True, max_length=20, null=True),
        ),
    ]
