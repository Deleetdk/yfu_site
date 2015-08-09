# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('cruise2016', '0005_auto_20150809_1251'),
    ]

    operations = [
        migrations.AlterField(
            model_name='signup',
            name='id',
            field=models.AutoField(serialize=False, primary_key=True),
        ),
    ]
