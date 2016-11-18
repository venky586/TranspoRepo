# -*- coding: utf-8 -*-
# Generated by Django 1.9.11 on 2016-11-18 17:56
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='CabDetails',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('empId', models.CharField(max_length=200)),
                ('empName', models.CharField(max_length=200)),
                ('gender', models.CharField(max_length=200)),
                ('tripType', models.CharField(max_length=200)),
                ('rosterDate', models.DateTimeField(blank=True, null=True)),
                ('tripTime', models.CharField(max_length=200)),
                ('locality', models.CharField(max_length=200)),
                ('cabRegNo', models.CharField(max_length=200)),
                ('cabType', models.CharField(max_length=200)),
                ('cabSerialNo', models.CharField(max_length=200)),
                ('publishDate', models.DateTimeField(blank=True, null=True)),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
