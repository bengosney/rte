# Generated by Django 3.0.2 on 2020-01-16 21:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('strava', '0007_auto_20200115_2138'),
    ]

    operations = [
        migrations.AlterField(
            model_name='runner',
            name='access_token',
            field=models.CharField(max_length=512),
        ),
        migrations.AlterField(
            model_name='runner',
            name='refresh_token',
            field=models.CharField(max_length=512),
        ),
    ]
