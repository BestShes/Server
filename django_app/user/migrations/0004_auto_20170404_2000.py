# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-04-04 11:00
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0003_remove_member_access_token'),
    ]

    operations = [
        migrations.AlterField(
            model_name='member',
            name='nickname',
            field=models.CharField(max_length=20),
        ),
    ]