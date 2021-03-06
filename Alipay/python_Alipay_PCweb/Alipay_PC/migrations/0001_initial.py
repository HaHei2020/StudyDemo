# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2017-11-21 08:38
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Orderinfo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('in_trade_no', models.CharField(blank=True, max_length=64, null=True)),
                ('trade_no', models.CharField(blank=True, max_length=64, null=True)),
                ('out_trade_no', models.CharField(blank=True, max_length=64, null=True)),
                ('product_code', models.CharField(blank=True, max_length=64, null=True)),
                ('subject', models.CharField(blank=True, max_length=256, null=True)),
                ('total_amount', models.DecimalField(blank=True, decimal_places=2, max_digits=10, null=True)),
                ('username', models.CharField(blank=True, max_length=100, null=True)),
                ('rechargetime', models.DateTimeField(blank=True, db_column='rechargeTime', null=True)),
                ('status', models.IntegerField(blank=True, null=True)),
                ('createtime', models.DateTimeField(blank=True, db_column='createTime', null=True)),
            ],
            options={
                'db_table': 'OrderInfo',
                'managed': False,
            },
        ),
    ]
