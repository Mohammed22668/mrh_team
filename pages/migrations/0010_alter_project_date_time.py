# Generated by Django 4.0 on 2022-01-06 18:06

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pages', '0009_alter_project_date_time'),
    ]

    operations = [
        migrations.AlterField(
            model_name='project',
            name='date_time',
            field=models.DateTimeField(default=datetime.datetime(2022, 1, 6, 21, 6, 54, 166210)),
        ),
    ]