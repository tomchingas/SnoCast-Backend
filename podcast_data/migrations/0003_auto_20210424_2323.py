# Generated by Django 3.2 on 2021-04-24 23:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('podcast_data', '0002_auto_20210422_0127'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='avalanche_accident',
            name='Lat',
        ),
        migrations.RemoveField(
            model_name='avalanche_accident',
            name='Long',
        ),
        migrations.AddField(
            model_name='avalanche_accident',
            name='Date',
            field=models.CharField(default='INPUT DATE', max_length=20),
        ),
        migrations.AddField(
            model_name='avalanche_accident',
            name='State',
            field=models.CharField(default='INPUT STATE', max_length=50),
        ),
        migrations.AlterField(
            model_name='avalanche_accident',
            name='Name',
            field=models.CharField(default='INPUT NAME', max_length=400),
        ),
    ]