# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Folder',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=50, verbose_name=b'Name')),
                ('parent', models.ForeignKey(related_name='children', verbose_name=b'\xc3\x9cberordner', blank=True, to='django_folders.Folder', null=True)),
            ],
            options={
                'ordering': ['name'],
                'verbose_name': 'Ordner',
                'verbose_name_plural': 'Ordner',
            },
        ),
    ]
