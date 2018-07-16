# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-04-20 08:34
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('ecom', '0002_auto_20180420_1216'),
    ]

    operations = [
        migrations.CreateModel(
            name='Cart',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Cartitem',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Cart', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='ecom.Cart')),
            ],
        ),
        migrations.CreateModel(
            name='Cartmodel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quantity', models.IntegerField()),
                ('Cart', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='ecom.Product')),
            ],
        ),
        migrations.RenameModel(
            old_name='Userdetails',
            new_name='user_details',
        ),
        migrations.AddField(
            model_name='cartitem',
            name='product',
            field=models.ManyToManyField(to='ecom.Cartmodel'),
        ),
    ]