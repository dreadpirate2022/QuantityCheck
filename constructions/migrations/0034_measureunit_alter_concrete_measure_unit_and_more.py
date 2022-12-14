# Generated by Django 4.1.2 on 2022-11-30 07:38

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('constructions', '0033_delete_measureunit_remove_concrete_measure_unit_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='MeasureUnit',
            fields=[
                ('name', models.CharField(blank=True, max_length=15, null=True)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False, unique=True)),
            ],
            options={
                'ordering': ['-created'],
            },
        ),
        migrations.AlterField(
            model_name='concrete',
            name='measure_unit',
            field=models.CharField(blank=True, max_length=10, null=True),
        ),
        migrations.AlterField(
            model_name='earth',
            name='measure_unit',
            field=models.CharField(blank=True, max_length=10, null=True),
        ),
        migrations.AlterField(
            model_name='others',
            name='measure_unit',
            field=models.CharField(blank=True, max_length=10, null=True),
        ),
        migrations.AlterField(
            model_name='reinforcement',
            name='measure_unit',
            field=models.CharField(blank=True, max_length=10, null=True),
        ),
    ]
