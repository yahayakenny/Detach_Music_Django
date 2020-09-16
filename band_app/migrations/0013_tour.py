# Generated by Django 3.1.1 on 2020-09-16 08:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('band_app', '0012_team'),
    ]

    operations = [
        migrations.CreateModel(
            name='Tour',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(blank=True, null=True, upload_to='')),
                ('name', models.CharField(blank=True, max_length=50, null=True)),
                ('date', models.CharField(blank=True, max_length=50, null=True)),
                ('venue', models.CharField(blank=True, max_length=50, null=True)),
                ('description', models.CharField(blank=True, max_length=200, null=True)),
            ],
        ),
    ]
