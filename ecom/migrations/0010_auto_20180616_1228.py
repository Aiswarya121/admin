# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-06-16 06:58
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('ecom', '0009_auto_20180615_2042'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cartm',
            name='product',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='ecom.Product'),
        ),
    ]
