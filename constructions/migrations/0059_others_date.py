# Generated by Django 4.1.2 on 2022-12-02 07:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('constructions', '0058_reinforcement_date'),
    ]

    operations = [
        migrations.AddField(
            model_name='others',
            name='date',
            field=models.DateField(blank=True, null=True),
        ),
    ]
