# Generated by Django 5.1.6 on 2025-07-04 14:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sampleapp', '0005_library'),
    ]

    operations = [
        migrations.CreateModel(
            name='Hospital',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30)),
                ('place', models.CharField(max_length=30)),
                ('age', models.IntegerField()),
            ],
        ),
    ]
