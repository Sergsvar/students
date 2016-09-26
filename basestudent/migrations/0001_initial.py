# -*- coding: utf-8 -*-
# Generated by Django 1.10.1 on 2016-09-26 10:05
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Abstract',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
        ),
        migrations.CreateModel(
            name='Group',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('group_name', models.CharField(max_length=22)),
            ],
        ),
        migrations.CreateModel(
            name='Student',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=55)),
                ('last_name', models.CharField(max_length=55)),
                ('father_name', models.CharField(max_length=55)),
                ('birthday', models.DateField(blank=True, null=True)),
                ('ticket_number', models.CharField(max_length=15)),
                ('student_group', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='basestudent.Group')),
            ],
        ),
        migrations.AddField(
            model_name='group',
            name='starosta',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='basestudent.Student'),
        ),
    ]