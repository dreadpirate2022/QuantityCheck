# Generated by Django 4.1.2 on 2022-11-18 11:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('constructions', '0029_alter_concrete_options_alter_construction_options_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='construction',
            name='tags',
            field=models.ManyToManyField(blank=True, max_length=20, to='constructions.tag'),
        ),
    ]
