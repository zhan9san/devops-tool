# Generated by Django 3.1.2 on 2020-11-18 16:11

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('environments', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='environment',
            name='description',
        ),
    ]