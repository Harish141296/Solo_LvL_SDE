# Generated by Django 5.2.3 on 2025-06-24 17:54

import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Quest',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('description', models.TextField(blank=True)),
                ('date', models.DateField(default=django.utils.timezone.now)),
                ('is_completed', models.BooleanField(default=False)),
            ],
        ),
    ]
