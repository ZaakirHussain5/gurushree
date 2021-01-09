# Generated by Django 3.0.5 on 2020-12-07 13:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('transactions', '0006_auto_20201207_1244'),
    ]

    operations = [
        migrations.AlterField(
            model_name='billdetails',
            name='Amount',
            field=models.DecimalField(decimal_places=2, max_digits=10, null=True),
        ),
        migrations.AlterField(
            model_name='billdetails',
            name='NetAmount',
            field=models.DecimalField(decimal_places=2, max_digits=10, null=True),
        ),
        migrations.AlterField(
            model_name='billdetails',
            name='PaidAmount',
            field=models.DecimalField(decimal_places=2, max_digits=10, null=True),
        ),
        migrations.AlterField(
            model_name='billdetails',
            name='TotalAmount',
            field=models.DecimalField(decimal_places=2, max_digits=10, null=True),
        ),
        migrations.AlterField(
            model_name='billheader',
            name='Balance',
            field=models.DecimalField(decimal_places=2, max_digits=10, null=True),
        ),
        migrations.AlterField(
            model_name='billheader',
            name='NetAmount',
            field=models.DecimalField(decimal_places=2, max_digits=10, null=True),
        ),
        migrations.AlterField(
            model_name='billheader',
            name='PaidAmount',
            field=models.DecimalField(decimal_places=2, max_digits=10, null=True),
        ),
        migrations.AlterField(
            model_name='billheader',
            name='Payable',
            field=models.DecimalField(decimal_places=2, max_digits=10, null=True),
        ),
    ]
