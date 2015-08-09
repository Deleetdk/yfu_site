# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('cruise2016', '0003_auto_20150808_2300'),
    ]

    operations = [
        migrations.RenameField(
            model_name='signup',
            old_name='user_email',
            new_name='email',
        ),
        migrations.RenameField(
            model_name='signup',
            old_name='hostparent_email',
            new_name='host_email',
        ),
        migrations.RenameField(
            model_name='signup',
            old_name='user_phone',
            new_name='phone',
        ),
    ]
