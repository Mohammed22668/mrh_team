# Generated by Django 4.0 on 2021-12-24 11:29

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pages', '0002_project_category_project_date_time_project_img1'),
    ]

    operations = [
        migrations.AddField(
            model_name='project',
            name='img2',
            field=models.ImageField(default='photos/%y/%m/%d', upload_to='photos/%y/%m/%d'),
        ),
        migrations.AddField(
            model_name='project',
            name='img3',
            field=models.ImageField(default='photos/%y/%m/%d', upload_to='photos/%y/%m/%d'),
        ),
        migrations.AddField(
            model_name='project',
            name='img4',
            field=models.ImageField(default='photos/%y/%m/%d', upload_to='photos/%y/%m/%d'),
        ),
        migrations.AlterField(
            model_name='project',
            name='date_time',
            field=models.DateTimeField(default=datetime.datetime(2021, 12, 24, 14, 29, 16, 141304)),
        ),
    ]
