# Generated by Django 4.1.2 on 2022-11-10 07:39

from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('constructions', '0027_reinforcement'),
    ]

    operations = [
        migrations.CreateModel(
            name='Others',
            fields=[
                ('name', models.CharField(max_length=50)),
                ('custom_name', models.CharField(blank=True, max_length=50, null=True)),
                ('quantity', models.DecimalField(blank=True, decimal_places=3, max_digits=50, null=True)),
                ('measure_unit', models.CharField(max_length=10)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False, unique=True)),
                ('owner', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='constructions.construction')),
            ],
        ),
    ]
