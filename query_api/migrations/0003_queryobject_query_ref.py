# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-03-05 01:01
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('query_api', '0002_query'),
    ]

    operations = [
        migrations.AddField(
            model_name='queryobject',
            name='query_ref',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='query', to='query_api.Query'),
            preserve_default=False,
        ),
    ]
