# -*- coding: utf-8 -*-
# Generated by Django 1.9.10 on 2016-10-31 20:27
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('incidents', '0006_merge'),
    ]

    operations = [
        migrations.CreateModel(
            name='NmapFile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('starttime', models.DateTimeField()),
                ('host', models.GenericIPAddressField()),
                ('port', models.IntegerField()),
                ('service', models.CharField(max_length=200)),
                ('flag', models.BooleanField()),
                ('scandate', models.DateField()),
            ],
        ),
    ]
