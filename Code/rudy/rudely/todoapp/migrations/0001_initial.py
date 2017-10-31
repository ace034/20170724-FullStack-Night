# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2017-10-12 02:27
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='TodoItem',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('question_text', models.CharField(max_length=200)),
                ('date_entered', models.DateTimeField(verbose_name='date entered')),
                ('date_completed', models.DateTimeField(verbose_name='date completed')),
                ('completed', models.BooleanField()),
            ],
        ),
    ]