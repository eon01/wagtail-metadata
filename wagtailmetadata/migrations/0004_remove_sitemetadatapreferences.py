# -*- coding: utf-8 -*-
# Generated by Django 1.10.1 on 2016-10-19 04:04


from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('wagtailmetadata', '0003_auto_20160909_1000'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='sitemetadatapreferences',
            name='site',
        ),
        migrations.RemoveField(
            model_name='sitemetadatapreferences',
            name='site_image',
        ),
        migrations.DeleteModel(
            name='SiteMetadataPreferences',
        ),
    ]
