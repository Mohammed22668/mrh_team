# Generated by Django 4.0 on 2022-01-12 16:01

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pages', '0011_alter_project_date_time'),
    ]

    operations = [
        migrations.AlterField(
            model_name='project',
            name='date_time',
            field=models.DateTimeField(default=datetime.datetime(2022, 1, 12, 19, 1, 17, 529626)),
        ),
    ]
