# Generated by Django 3.0.5 on 2020-12-24 10:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('transactions', '0017_auto_20201224_1232'),
    ]

    operations = [
        migrations.AlterField(
            model_name='billreceipt',
            name='OtherBank',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
    ]
