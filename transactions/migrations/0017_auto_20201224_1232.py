# Generated by Django 3.0.5 on 2020-12-24 07:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('transactions', '0016_bookappointments'),
    ]

    operations = [
        migrations.AlterField(
            model_name='billreceipt',
            name='RecAmount',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=10, null=True),
        ),
    ]