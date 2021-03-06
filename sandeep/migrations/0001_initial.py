# -*- coding: utf-8 -*-
# Generated by Django 1.9.1 on 2016-01-27 21:54
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('email', models.CharField(max_length=60)),
                ('image', models.FileField(upload_to='static/img/profile/')),
                ('about', models.TextField(null=True)),
                ('password', models.CharField(max_length=100)),
                ('address', models.TextField(null=True)),
                ('phone', models.CharField(max_length=30)),
                ('when', models.DateTimeField(auto_now_add=True, verbose_name='date created')),
            ],
        ),
        migrations.CreateModel(
            name='Project',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('user_id', models.IntegerField()),
                ('image', models.FileField(upload_to='static/img/projects/')),
                ('about', models.TextField(null=True)),
                ('start_date', models.DateField()),
                ('end_date', models.DateField()),
                ('when', models.DateTimeField(auto_now_add=True, verbose_name='date created')),
            ],
        ),
    ]
