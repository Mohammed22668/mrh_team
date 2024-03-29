# Generated by Django 4.0 on 2022-09-11 21:21

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
        ('pages', '0014_alter_members_mmname_alter_posts_pdata_time_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='members',
            name='MMfullname',
            field=models.CharField(blank=True, max_length=150, verbose_name='الاسم الكامل'),
        ),
        migrations.AlterField(
            model_name='members',
            name='MMname',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='auth.user', verbose_name='الاسم'),
        ),
        migrations.AlterField(
            model_name='posts',
            name='Pdata_time',
            field=models.DateTimeField(default=datetime.datetime(2022, 9, 12, 0, 21, 22, 944588)),
        ),
        migrations.AlterField(
            model_name='project',
            name='date_time',
            field=models.DateTimeField(default=datetime.datetime(2022, 9, 12, 0, 21, 22, 934522)),
        ),
    ]
