# Generated by Django 4.0.4 on 2022-05-27 12:41

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('groups', '0003_alter_group_date_of_start_alter_group_group_name_and_more'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='group',
            options={'verbose_name': 'group', 'verbose_name_plural': 'groups'},
        ),
    ]
