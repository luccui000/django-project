# -*- coding: utf-8 -*-
# Generated by Django 1.11.25 on 2019-12-24 07:12
from __future__ import unicode_literals

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0003_auto_20191212_1032'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='thoigiandangbai',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
    ]
