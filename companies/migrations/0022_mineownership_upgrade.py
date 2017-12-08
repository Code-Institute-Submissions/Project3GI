# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2017-11-30 04:12
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('mining', '0009_remove_mine_upgrade'),
        ('companies', '0021_planettrade'),
    ]

    operations = [
        migrations.AddField(
            model_name='mineownership',
            name='upgrade',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='mining.Upgrade'),
        ),
    ]
