# Generated by Django 4.2.11 on 2025-01-17 17:23

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='member',
            name='mobile_no',
            field=models.IntegerField(validators=[django.core.validators.MinLengthValidator(0), django.core.validators.MaxLengthValidator(9999999999)]),
        ),
    ]
