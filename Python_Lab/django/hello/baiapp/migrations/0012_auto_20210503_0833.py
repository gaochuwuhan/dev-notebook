# Generated by Django 3.1.7 on 2021-05-03 08:33

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('baiapp', '0011_auto_20210424_1748'),
    ]

    operations = [
        migrations.RenameField(
            model_name='tag',
            old_name='created_name',
            new_name='created_time',
        ),
    ]
