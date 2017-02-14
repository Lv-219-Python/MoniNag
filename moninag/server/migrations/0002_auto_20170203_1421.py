# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-02-03 12:21
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('server', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='server',
            name='user',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='server',
            name='state',
            field=models.CharField(choices=[('', 'NotSelected'), ('prod', 'Production'), ('stag', 'Staging')], default='', max_length=20),
        ),
    ]
