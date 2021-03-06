# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2016-12-07 12:21
from __future__ import unicode_literals

from decimal import Decimal
from django.db import migrations
#import djmoney.models.fields
from django.db import migrations, models

class Migration(migrations.Migration):

    dependencies = [
        ('core', '0015_auto_20161207_1220'),
    ]

    operations = [
        migrations.AddField(
            model_name='transaction',
            name='settlement_ammount_currency',
            field=models.DecimalField(decimal_places=2, default=0.0, max_digits=8),
        ),
        migrations.AddField(
            model_name='transaction',
            name='vat_ammount_currency',
            field=models.DecimalField(decimal_places=2, default=0.0, max_digits=8),
        ),
        migrations.AlterField(
            model_name='transaction',
            name='settlement_ammount',
            field=models.DecimalField(decimal_places=2, default=0.0, max_digits=8),
        ),
        migrations.AlterField(
            model_name='transaction',
            name='vat_ammount',
            field=models.DecimalField(decimal_places=2, default=0.0, max_digits=8),
        ),
    ]
