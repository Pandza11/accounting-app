# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2016-12-22 09:27
from __future__ import unicode_literals

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0023_auto_20161221_1523'),
    ]

    operations = [
        migrations.AlterField(
            model_name='transaction',
            name='invoice_date',
            field=models.DateField(default=datetime.datetime.today, verbose_name='Invoice date'),
        ),
    ]
