# Generated by Django 3.1.2 on 2020-11-18 16:11

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('deployments', '0004_auto_20201118_0334'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='currentpackage',
            name='description',
        ),
        migrations.RemoveField(
            model_name='currentpackage',
            name='name',
        ),
        migrations.RemoveField(
            model_name='deployment',
            name='description',
        ),
        migrations.RemoveField(
            model_name='deployment',
            name='name',
        ),
    ]
