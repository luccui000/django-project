# -*- coding: utf-8 -*-
# Generated by Django 1.11.25 on 2019-12-25 00:04
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0008_product_active'),
    ]

    operations = [
        migrations.RenameField(
            model_name='product',
            old_name=b'motasp',
            new_name='description',
        ),
        migrations.RenameField(
            model_name='product',
            old_name='hinhsp',
            new_name='image',
        ),
        migrations.RenameField(
            model_name='product',
            old_name='thoigiandangbai',
            new_name='post_times',
        ),
        migrations.RenameField(
            model_name='product',
            old_name=b'giasp',
            new_name='price',
        ),
        migrations.RenameField(
            model_name='product',
            old_name=b'tieude',
            new_name='title',
        ),
    ]
