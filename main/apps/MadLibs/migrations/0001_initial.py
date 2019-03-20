# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2019-03-12 02:14
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Card',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sender', models.TextField(blank=True, max_length=30)),
                ('recipient', models.TextField(blank=True, max_length=30)),
                ('event', models.TextField(blank=True, max_length=30)),
                ('noun1', models.TextField(blank=True, max_length=30)),
                ('noun2', models.TextField(blank=True, max_length=30)),
                ('noun3', models.TextField(blank=True, max_length=30)),
                ('noun4', models.TextField(blank=True, max_length=30)),
                ('noun5', models.TextField(blank=True, max_length=30)),
                ('noun6', models.TextField(blank=True, max_length=30)),
                ('noun7', models.TextField(blank=True, max_length=30)),
                ('noun8', models.TextField(blank=True, max_length=30)),
                ('noun9', models.TextField(blank=True, max_length=30)),
                ('adj1', models.TextField(blank=True, max_length=30)),
                ('adj2', models.TextField(blank=True, max_length=30)),
                ('adj3', models.TextField(blank=True, max_length=30)),
                ('adj4', models.TextField(blank=True, max_length=30)),
                ('adj5', models.TextField(blank=True, max_length=30)),
                ('adj6', models.TextField(blank=True, max_length=30)),
                ('adj7', models.TextField(blank=True, max_length=30)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
            ],
        ),
    ]