# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2018-08-26 05:42
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('accounts', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Friend',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fid', models.IntegerField(null=True)),
                ('name', models.CharField(max_length=20, null=True)),
                ('username', models.CharField(max_length=30, null=True)),
                ('timestamp', models.DateField(auto_now=True)),
                ('profile', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='accounts.Profile')),
            ],
        ),
        migrations.CreateModel(
            name='RequestCall',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('coming_from', models.CharField(max_length=30)),
                ('coming_from_profile_id', models.CharField(max_length=10, null=True)),
                ('coming_for', models.CharField(max_length=30)),
                ('coming_for_profile_id', models.CharField(max_length=10, null=True)),
                ('coming_from_name', models.CharField(max_length=50, null=True)),
                ('coming_for_name', models.CharField(max_length=50, null=True)),
            ],
        ),
    ]
