# Generated by Django 5.1.6 on 2025-07-07 11:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sampleapp', '0008_book'),
    ]

    operations = [
        migrations.CreateModel(
            name='Shop',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('firstname', models.CharField(max_length=30)),
                ('lastname', models.CharField(max_length=30)),
                ('email', models.EmailField(max_length=50)),
                ('place', models.CharField(max_length=30)),
            ],
        ),
    ]
