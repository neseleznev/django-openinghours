# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
from openinghours.app_settings import PREMISES_MODEL

initial_operations = []
if PREMISES_MODEL == 'openinghours.Company':
    initial_operations = [
        migrations.CreateModel(
            name='Company',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=100)),
                ('slug', models.SlugField(unique=True)),
                ('logo', models.FileField(null=True, upload_to=b'logo', blank=True)),
            ],
            options={
                'verbose_name': 'Company',
                'verbose_name_plural': 'Companies',
            },
        ),
    ]

class Migration(migrations.Migration):
    dependencies = []
    operations = initial_operations + [
        migrations.CreateModel(
            name='ClosingRules',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('start', models.DateTimeField(verbose_name='Start')),
                ('end', models.DateTimeField(verbose_name='End')),
                ('reason', models.TextField(blank=True, null=True, verbose_name='Reason')),
                ('company', models.ForeignKey(to=PREMISES_MODEL)),
            ],
            options={
                'verbose_name': 'Closing Rule',
                'verbose_name_plural': 'Closing Rules',
                'ordering': ['start'],
            },
        ),
        migrations.CreateModel(
            name='OpeningHours',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('weekday', models.IntegerField(choices=[(1, 'Monday'), (2, 'Tuesday'), (3, 'Wednesday'), (4, 'Thursday'), (5, 'Friday'), (6, 'Saturday'), (7, 'Sunday')], verbose_name='Weekday')),
                ('from_hour', models.TimeField(verbose_name='Opening')),
                ('to_hour', models.TimeField(verbose_name='Closing')),
                ('company', models.ForeignKey(to=PREMISES_MODEL)),
            ],
            options={
                'verbose_name': 'Opening Hours',
                'verbose_name_plural': 'Opening Hours',
                'ordering': ['company', 'weekday', 'from_hour'],
            },
        ),
    ]
