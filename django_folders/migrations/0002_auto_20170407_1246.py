# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('django_folders', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='folder',
            name='parent',
            field=models.ForeignKey(related_name='children', verbose_name='\xdcberordner', blank=True, to='django_folders.Folder', null=True),
        ),
    ]
