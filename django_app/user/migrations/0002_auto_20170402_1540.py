# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-04-02 06:40
from __future__ import unicode_literals

from django.db import migrations
import user.models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelManagers(
            name='member',
            managers=[
                ('objects', user.models.MemberManager()),
            ],
        ),
    ]
