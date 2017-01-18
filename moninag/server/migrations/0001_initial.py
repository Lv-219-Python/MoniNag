# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-01-18 12:00
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Server',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('addrxess', models.CharField(max_length=200)),
                ('status', models.CharField(choices=[(1, 'NotSelected'), (2, 'Production'), (3, 'Staging')], default=0, max_length=100)),
            ],
        ),
    ]
