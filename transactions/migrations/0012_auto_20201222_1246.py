# Generated by Django 3.0.5 on 2020-12-22 07:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('transactions', '0011_auto_20201222_1245'),
    ]

    operations = [
        migrations.AlterField(
            model_name='billreceipt',
            name='CardBank',
            field=models.CharField(max_length=50, null=True),
        ),
    ]
