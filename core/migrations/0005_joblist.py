# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2017-04-10 17:18
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0004_auto_20170308_1007'),
    ]

    operations = [
        migrations.CreateModel(
            name='JobList',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('jobtitle', models.CharField(max_length=100)),
                ('jobdescription', models.TextField(max_length=300)),
                ('postdate', models.DateField(auto_now_add=True)),
            ],
        ),
    ]
