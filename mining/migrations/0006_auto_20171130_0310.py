# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2017-11-30 03:10
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('mining', '0005_mine_upgrade'),
    ]

    operations = [
        migrations.AlterField(
            model_name='mine',
            name='upgrade',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='mining.Upgrade'),
        ),
    ]