# Generated by Django 4.1.2 on 2022-10-26 12:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('constructions', '0002_tag_construction_tags'),
    ]

    operations = [
        migrations.AddField(
            model_name='construction',
            name='featured_image',
            field=models.ImageField(blank=True, default='default.jpg', null=True, upload_to=''),
        ),
    ]
