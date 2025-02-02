# Generated by Django 5.1.5 on 2025-02-02 20:59

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='City',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('city_name', models.CharField(max_length=100, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='NGO',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ngo_name', models.CharField(max_length=255)),
                ('ngo_description', models.TextField()),
                ('ngo_city_name', models.ForeignKey(default='string', on_delete=django.db.models.deletion.CASCADE, to='api.city')),
            ],
        ),
    ]
