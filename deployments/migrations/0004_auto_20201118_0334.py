# Generated by Django 3.1.2 on 2020-11-18 03:34

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('environments', '0001_initial'),
        ('applications', '0002_auto_20201117_0743'),
        ('deployments', '0003_auto_20201118_0247'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='History',
            new_name='Deployment',
        ),
    ]
