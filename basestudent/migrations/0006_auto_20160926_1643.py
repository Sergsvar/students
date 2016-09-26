# -*- coding: utf-8 -*-
# Generated by Django 1.10.1 on 2016-09-26 16:43
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('basestudent', '0005_auto_20160926_1640'),
    ]

    operations = [
        migrations.AlterField(
            model_name='student',
            name='student_group',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='basestudent.Group', verbose_name='Группа, к которой прикреплен студент'),
        ),
    ]
