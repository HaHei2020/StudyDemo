# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2017-10-31 10:32
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('slg', '0006_auto_20171031_0937'),
    ]

    operations = [
        migrations.AlterModelTable(
            name='permission',
            table='slg_permission',
        ),
    ]
