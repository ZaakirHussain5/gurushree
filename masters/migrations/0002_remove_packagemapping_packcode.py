# Generated by Django 2.2.12 on 2020-06-24 14:43

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('masters', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='packagemapping',
            name='PackCode',
        ),
    ]
