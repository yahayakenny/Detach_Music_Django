# Generated by Django 3.1.1 on 2020-09-15 10:04

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('band_app', '0002_auto_20200915_0942'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='event',
            name='hero_text',
        ),
    ]
