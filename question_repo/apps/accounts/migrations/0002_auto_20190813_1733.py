# -*- coding: utf-8 -*-
# Generated by Django 1.11.20 on 2019-08-13 09:33
from __future__ import unicode_literals

from django.db import migrations
import easy_thumbnails.fields


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='avator_sor',
            field=easy_thumbnails.fields.ThumbnailerImageField(default='avator/default.jpg', upload_to='avator/%Y%m%d/', verbose_name='头像'),
        ),
    ]
