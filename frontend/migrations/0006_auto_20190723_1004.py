# -*- coding: utf-8 -*-
# Generated by Django 1.11.16 on 2019-07-23 10:04
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('frontend', '0005_auto_20190723_1004'),
    ]

    operations = [
        migrations.AlterField(
            model_name='users',
            name='name',
            field=models.CharField(max_length=100, unique=True),
        ),
    ]
