# Generated by Django 3.0.5 on 2020-05-18 19:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('film', '0008_auto_20200518_1451'),
    ]

    operations = [
        migrations.AlterField(
            model_name='movie',
            name='movie_title',
            field=models.CharField(default='About Me', max_length=200),
        ),
    ]
