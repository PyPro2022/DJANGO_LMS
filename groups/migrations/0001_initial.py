# Generated by Django 4.0.4 on 2022-05-20 21:07

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Group',
            fields=[
                ('group_id', models.BigAutoField(primary_key=True, serialize=False)),
                ('group_name', models.CharField(max_length=100)),
                ('date_of_start', models.DateField()),
            ],
        ),
    ]
