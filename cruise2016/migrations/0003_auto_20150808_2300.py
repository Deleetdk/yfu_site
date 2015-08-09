# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('cruise2016', '0002_signup_paid'),
    ]

    operations = [
        migrations.AddField(
            model_name='signup',
            name='gender',
            field=models.CharField(max_length=6, default='Male'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='signup',
            name='excursion_1',
            field=models.CharField(max_length=200),
        ),
        migrations.AlterField(
            model_name='signup',
            name='excursion_2',
            field=models.CharField(max_length=200),
        ),
        migrations.AlterField(
            model_name='signup',
            name='excursion_3',
            field=models.CharField(max_length=200),
        ),
        migrations.AlterField(
            model_name='signup',
            name='paid',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='signup',
            name='signup_date',
            field=models.DateTimeField(),
        ),
    ]
