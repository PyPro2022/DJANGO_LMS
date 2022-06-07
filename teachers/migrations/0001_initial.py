# Generated by Django 4.0.4 on 2022-06-07 14:47

import core.validators
import datetime
import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Teacher',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(db_column='first_name', max_length=100, validators=[django.core.validators.MinLengthValidator(2)], verbose_name='first name')),
                ('last_name', models.CharField(db_column='last_name', max_length=100, validators=[django.core.validators.MinLengthValidator(2)], verbose_name='last name')),
                ('birthday', models.DateField(default=datetime.date.today, validators=[core.validators.adult_validator], verbose_name='birthday')),
                ('phone_number', models.CharField(blank=True, max_length=20, null=True, validators=[django.core.validators.MinLengthValidator(10), core.validators.uniqness_validator], verbose_name='phone number')),
                ('salary', models.PositiveIntegerField(default=10000)),
            ],
            options={
                'verbose_name': 'teacher',
                'verbose_name_plural': 'teachers',
                'db_table': 'teachers',
            },
        ),
    ]
