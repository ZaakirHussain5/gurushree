# Generated by Django 3.0.5 on 2020-12-18 10:27

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('transactions', '0007_auto_20201207_1841'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='billreceipt',
            name='RecDate',
        ),
        migrations.RemoveField(
            model_name='billreceipt',
            name='RecTime',
        ),
    ]