# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2016-12-07 12:20
from __future__ import unicode_literals

import core.models
from decimal import Decimal
from django.db import migrations, models
#import djmoney.models.fields


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0014_auto_20161207_1053'),
    ]

    operations = [
        migrations.AlterField(
            model_name='transaction',
            name='end_date',
            field=models.DateField(default='core.models.Transaction.last_day_of_month', verbose_name='End date'),
        ),
        migrations.AlterField(
            model_name='transaction',
            name='start_date',
            field=models.DateField(default='core.models.Transaction.first_day_of_month', verbose_name='Start date'),
        ),
    ]
