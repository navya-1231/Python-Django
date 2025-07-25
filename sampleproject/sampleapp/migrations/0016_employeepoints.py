# Generated by Django 5.1.6 on 2025-07-10 05:04

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sampleapp', '0015_employee'),
    ]

    operations = [
        migrations.CreateModel(
            name='EmployeePoints',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('points', models.IntegerField()),
                ('employee', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='points', to='sampleapp.employee')),
            ],
        ),
    ]
