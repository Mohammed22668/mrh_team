# Generated by Django 4.0 on 2021-12-24 17:48

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
        ('pages', '0004_project_detail_alter_project_date_time'),
    ]

    operations = [
        migrations.AlterField(
            model_name='project',
            name='date_time',
            field=models.DateTimeField(default=datetime.datetime(2021, 12, 24, 20, 48, 24, 384553)),
        ),
        migrations.AlterField(
            model_name='project',
            name='detail',
            field=models.TextField(blank=True, max_length=250, null=True, verbose_name='التفاصيل'),
        ),
        migrations.CreateModel(
            name='Rusul',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('info', models.TextField(blank=True, max_length=500, verbose_name='المعلومات')),
                ('Rimg', models.ImageField(upload_to='photos/%y/%m/%d', verbose_name='الصورة')),
                ('Rname', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='auth.user', verbose_name='الاسم')),
            ],
        ),
        migrations.CreateModel(
            name='Mohammed',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Minfo', models.TextField(blank=True, max_length=500, verbose_name='المعلومات')),
                ('Mimg', models.ImageField(upload_to='photos/%y/%m/%d', verbose_name='الصورة')),
                ('Mname', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='auth.user', verbose_name='الاسم')),
            ],
        ),
        migrations.CreateModel(
            name='Hussain',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Hinfo', models.TextField(blank=True, max_length=500, verbose_name='المعلومات')),
                ('Himg', models.ImageField(upload_to='photos/%y/%m/%d', verbose_name='الصورة')),
                ('Hname', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='auth.user', verbose_name='الاسم')),
            ],
        ),
    ]
