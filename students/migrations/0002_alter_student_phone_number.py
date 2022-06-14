# Generated by Django 4.0.4 on 2022-05-21 10:00

import django.core.validators
from django.db import migrations, models
import students.validators


class Migration(migrations.Migration):

    dependencies = [
        ('students', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='student',
            name='phone_number',
            field=models.CharField(default='', max_length=20, validators=[django.core.validators.MinLengthValidator(10), students.validators.uniqness_validator], verbose_name='st_ph_number'),
        ),
    ]
