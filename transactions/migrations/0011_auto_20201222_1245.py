# Generated by Django 3.0.5 on 2020-12-22 07:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('transactions', '0010_auto_20201222_1240'),
    ]

    operations = [
        migrations.AlterField(
            model_name='billreceipt',
            name='OtherPayNo',
            field=models.CharField(blank=True, max_length=32, null=True),
        ),
    ]
