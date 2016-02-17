# -*- coding: utf-8 -*-
# Generated by Django 1.9.2 on 2016-02-17 14:02
from __future__ import unicode_literals

from django.db import migrations
import django.db.models.deletion
import filer.fields.image


class Migration(migrations.Migration):

    dependencies = [
        ('course', '0005_auto_20160217_0850'),
    ]

    operations = [
        migrations.AlterField(
            model_name='course',
            name='art',
            field=filer.fields.image.FilerImageField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='filer.Image'),
        ),
    ]