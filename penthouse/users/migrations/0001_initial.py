# Generated by Django 4.2.11 on 2025-01-17 17:16

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Member',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user_id', models.CharField(max_length=50)),
                ('full_name', models.CharField(max_length=200)),
                ('address', models.CharField(max_length=500)),
                ('mobile_no', models.IntegerField(max_length=10, validators=[django.core.validators.MinLengthValidator(10)])),
                ('password', models.CharField(max_length=16, validators=[django.core.validators.MinLengthValidator(8)])),
            ],
        ),
    ]
