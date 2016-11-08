# -*- coding: utf-8 -*-
# Generated by Django 1.9.10 on 2016-11-06 15:38
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('incidents', '0010_nessusfile'),
    ]

    operations = [
        migrations.CreateModel(
            name='AWVSFile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('scantime', models.CharField(max_length=30)),
                ('scanurl', models.CharField(max_length=20)),
                ('operatingOS', models.CharField(max_length=50)),
                ('webserver', models.CharField(max_length=30)),
                ('itemname', models.CharField(max_length=100)),
                ('severity', models.CharField(max_length=6)),
                ('details', models.CharField(max_length=1024)),
                ('description', models.CharField(max_length=1024)),
                ('recommendation', models.CharField(max_length=1024)),
                ('existence', models.BooleanField()),
            ],
        ),
    ]
