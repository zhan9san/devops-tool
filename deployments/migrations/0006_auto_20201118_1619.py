# Generated by Django 3.1.2 on 2020-11-18 16:19

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('deployments', '0005_auto_20201118_1611'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='currentpackage',
            name='project',
        ),
        migrations.RemoveField(
            model_name='deployment',
            name='project',
        ),
    ]
