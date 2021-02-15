# Generated by Django 3.0.5 on 2020-05-18 18:51

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('film', '0007_auto_20200509_1338'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='movie',
            name='date_uploaded',
        ),
        migrations.AlterField(
            model_name='movie',
            name='movie',
            field=models.FileField(null=True, upload_to='videos/', validators=[django.core.validators.FileExtensionValidator(allowed_extensions=['mp4', 'mov'])], verbose_name=''),
        ),
    ]