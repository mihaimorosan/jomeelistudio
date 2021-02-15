# Generated by Django 3.0.8 on 2020-08-11 23:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('photography', '0008_auto_20200810_1849'),
    ]

    operations = [
        migrations.AddField(
            model_name='creative',
            name='slug',
            field=models.SlugField(null=True),
        ),
        migrations.AlterField(
            model_name='creative',
            name='project_thumbnail',
            field=models.ImageField(default=None, upload_to='images/photography/creative/project-thumbnails/'),
        ),
    ]