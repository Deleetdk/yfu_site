# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('cruise2016', '0004_auto_20150809_0101'),
    ]

    operations = [
        migrations.AlterField(
            model_name='signup',
            name='host_email',
            field=models.EmailField(null=True, max_length=254),
        ),
        migrations.AlterField(
            model_name='signup',
            name='host_name',
            field=models.CharField(null=True, max_length=200),
        ),
        migrations.AlterField(
            model_name='signup',
            name='host_phone',
            field=models.CharField(null=True, max_length=200),
        ),
    ]
