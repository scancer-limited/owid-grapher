# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-07-24 05:08
from __future__ import unicode_literals

from django.db import migrations

class Migration(migrations.Migration):
    dependencies = [
        ('grapher_admin', '0046_merge_20180320_0632'),
    ]

    operations = [
        migrations.RunSQL("""
            ALTER TABLE datasets ADD isPrivate BOOLEAN NOT NULL DEFAULT FALSE
        """)
    ]
