# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-04-05 22:38
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Post',
            new_name='Book',
        ),
    ]
