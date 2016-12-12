# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2016-12-07 12:26
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0016_auto_20161207_1221'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='transaction',
            name='invoice_amount_currency',
        ),
        migrations.RemoveField(
            model_name='transaction',
            name='settlement_ammount_currency',
        ),
        migrations.RemoveField(
            model_name='transaction',
            name='vat_ammount_currency',
        ),
        migrations.AlterField(
            model_name='transaction',
            name='invoice_amount',
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