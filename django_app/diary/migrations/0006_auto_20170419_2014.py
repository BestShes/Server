# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-04-19 11:14
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('diary', '0005_auto_20170419_1609'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='created_date',
            field=models.DateTimeField(default='2017-04-19 20:14'),
        ),
    ]
