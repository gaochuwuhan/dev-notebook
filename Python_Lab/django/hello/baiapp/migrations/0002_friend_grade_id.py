# Generated by Django 3.1.5 on 2021-01-31 11:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('baiapp', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='friend',
            name='grade_id',
            field=models.IntegerField(default=6),
        ),
    ]
