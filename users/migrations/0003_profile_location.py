# Generated by Django 4.1.2 on 2022-11-01 10:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0002_profile_username_alter_profile_name'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='location',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
    ]
