# Generated by Django 3.1.1 on 2020-09-15 10:09

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('band_app', '0004_auto_20200915_1007'),
    ]

    operations = [
        migrations.RenameField(
            model_name='event',
            old_name='image_eight',
            new_name='event_image',
        ),
        migrations.RemoveField(
            model_name='event',
            name='image_five',
        ),
        migrations.RemoveField(
            model_name='event',
            name='image_four',
        ),
        migrations.RemoveField(
            model_name='event',
            name='image_nine',
        ),
        migrations.RemoveField(
            model_name='event',
            name='image_one',
        ),
        migrations.RemoveField(
            model_name='event',
            name='image_seven',
        ),
        migrations.RemoveField(
            model_name='event',
            name='image_six',
        ),
        migrations.RemoveField(
            model_name='event',
            name='image_three',
        ),
        migrations.RemoveField(
            model_name='event',
            name='image_two',
        ),
    ]
