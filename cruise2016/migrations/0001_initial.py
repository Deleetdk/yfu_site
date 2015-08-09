# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='SignUp',
            fields=[
                ('id', models.AutoField(serialize=False, primary_key=True, verbose_name='ID', auto_created=True)),
                ('name', models.CharField(max_length=200)),
                ('age', models.CharField(max_length=2)),
                ('person_type', models.CharField(max_length=200)),
                ('user_phone', models.CharField(max_length=200)),
                ('user_email', models.EmailField(max_length=254)),
                ('host_name', models.CharField(max_length=200)),
                ('host_phone', models.CharField(max_length=200)),
                ('hostparent_email', models.EmailField(max_length=254)),
                ('total_family_members', models.CharField(max_length=2)),
                ('excursion_1', models.IntegerField()),
                ('excursion_2', models.IntegerField()),
                ('excursion_3', models.IntegerField()),
                ('price', models.IntegerField()),
                ('signup_date', models.DateField(auto_now=True)),
            ],
        ),
    ]
