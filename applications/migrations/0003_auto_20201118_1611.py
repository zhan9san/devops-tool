# Generated by Django 3.1.2 on 2020-11-18 16:11

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('applications', '0002_auto_20201117_0743'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='application',
            name='description',
        ),
        migrations.RemoveField(
            model_name='project',
            name='description',
        ),
    ]
