# Generated by Django 4.1.2 on 2022-12-08 07:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('constructions', '0060_alter_concrete_custom_name_alter_concrete_name_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='concrete',
            name='quantity',
            field=models.DecimalField(blank=True, decimal_places=2, default=0, max_digits=50, null=True),
        ),
        migrations.AlterField(
            model_name='earth',
            name='quantity',
            field=models.DecimalField(blank=True, decimal_places=2, default=0, max_digits=50, null=True),
        ),
        migrations.AlterField(
            model_name='others',
            name='quantity',
            field=models.DecimalField(blank=True, decimal_places=2, default=0, max_digits=50, null=True),
        ),
        migrations.AlterField(
            model_name='reinforcement',
            name='quantity',
            field=models.DecimalField(blank=True, decimal_places=2, default=0, max_digits=50, null=True),
        ),
    ]
