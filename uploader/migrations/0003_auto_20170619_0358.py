# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2017-06-19 08:58
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ('uploads', '0002_auto_20170406_0620'),
    ]

    operations = [
        migrations.AlterField(
            model_name='upload',
            name='upload_length',
            field=models.BigIntegerField(default=-1),
        ),
        migrations.AlterField(
            model_name='upload',
            name='upload_offset',
            field=models.BigIntegerField(default=0),
        ),
    ]
