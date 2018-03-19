# -*- coding: utf-8 -*-
# Generated by Django 1.11.11 on 2018-03-19 15:28
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('display', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='devices',
            name='status',
            field=models.IntegerField(default=2),
        ),
        migrations.AlterField(
            model_name='devices',
            name='location',
            field=models.IntegerField(default=1),
        ),
        migrations.AlterField(
            model_name='devices',
            name='name',
            field=models.CharField(default='请设置设备名<10字', max_length=10),
        ),
        migrations.AlterField(
            model_name='tips',
            name='tip',
            field=models.CharField(default='请设置提示栏<20字', max_length=20),
        ),
    ]