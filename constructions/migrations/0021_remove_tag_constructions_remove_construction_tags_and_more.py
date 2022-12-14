# Generated by Django 4.1.2 on 2022-11-07 20:00

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('constructions', '0020_tag_constructions'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='tag',
            name='constructions',
        ),
        migrations.RemoveField(
            model_name='construction',
            name='tags',
        ),
        migrations.AddField(
            model_name='construction',
            name='tags',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='constructions.tag'),
        ),
    ]
