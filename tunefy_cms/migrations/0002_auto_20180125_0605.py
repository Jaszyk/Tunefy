# Generated by Django 2.0.1 on 2018-01-25 05:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tunefy_cms', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='album',
            name='cover',
        ),
        migrations.RemoveField(
            model_name='album',
            name='cover_thumb',
        ),
        migrations.AlterField(
            model_name='genre',
            name='albums',
            field=models.ManyToManyField(blank=True, to='tunefy_cms.Album'),
        ),
    ]
