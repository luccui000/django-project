# -*- coding: utf-8 -*-
# Generated by Django 1.11.25 on 2019-12-28 08:10
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0009_auto_20191225_0004'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='slug',
            field=models.SlugField(default=b'abc', unique=True),
        ),
    ]
