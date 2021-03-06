# Generated by Django 2.2.12 on 2020-07-21 10:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('transactions', '0002_auto_20200710_0631'),
    ]

    operations = [
        migrations.CreateModel(
            name='billheader',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('BillNo', models.CharField(max_length=32, null=True)),
                ('BillDateTime', models.DateTimeField(auto_now_add=True)),
                ('BillDate', models.CharField(max_length=32, null=True)),
                ('BillTime', models.CharField(max_length=32, null=True)),
                ('RegNo', models.CharField(max_length=32, null=True)),
                ('RegType', models.CharField(max_length=32, null=True)),
                ('PayType', models.CharField(max_length=32, null=True)),
                ('DiscountBy', models.CharField(max_length=32, null=True)),
                ('DiscType', models.CharField(max_length=32, null=True)),
                ('DiscPerc', models.DecimalField(decimal_places=2, max_digits=18, null=True)),
                ('DiscNote', models.CharField(max_length=32, null=True)),
                ('TotalAmount', models.DecimalField(decimal_places=2, max_digits=18, null=True)),
                ('DrDiscount', models.DecimalField(decimal_places=2, max_digits=18, null=True)),
                ('ReferDiscount', models.DecimalField(decimal_places=2, max_digits=18, null=True)),
                ('HospDiscount', models.DecimalField(decimal_places=2, max_digits=5, null=True)),
                ('TotalDiscount', models.DecimalField(decimal_places=2, max_digits=5, null=True)),
                ('NetAmount', models.DecimalField(decimal_places=2, max_digits=5, null=True)),
                ('Payable', models.DecimalField(decimal_places=2, max_digits=5, null=True)),
                ('Balance', models.DecimalField(decimal_places=2, max_digits=5, null=True)),
                ('TPAName', models.CharField(max_length=32, null=True)),
                ('TPABalance', models.DecimalField(decimal_places=2, max_digits=5, null=True)),
                ('PaidAmount', models.DecimalField(decimal_places=2, max_digits=5, null=True)),
                ('Advance', models.DecimalField(decimal_places=2, max_digits=5, null=True)),
                ('TobeRefund', models.DecimalField(decimal_places=2, max_digits=5, null=True)),
                ('Refunded', models.DecimalField(decimal_places=2, max_digits=5, null=True)),
                ('Status', models.CharField(max_length=32, null=True)),
                ('CancelDate', models.DateTimeField(auto_now_add=True)),
                ('CancelUser', models.CharField(max_length=32, null=True)),
                ('CancelReason', models.CharField(max_length=32, null=True)),
                ('FY', models.CharField(max_length=32, null=True)),
                ('PatientName', models.CharField(max_length=32, null=True)),
                ('Age', models.CharField(max_length=32, null=True)),
                ('Year', models.IntegerField(null=True)),
                ('Month', models.IntegerField(null=True)),
                ('Days', models.IntegerField(null=True)),
                ('Address1', models.CharField(max_length=32, null=True)),
                ('IsActive', models.BooleanField(default=True)),
                ('AddedBy', models.CharField(max_length=32, null=True)),
                ('AddedOn', models.DateTimeField(auto_now_add=True)),
                ('EditedBy', models.CharField(max_length=32, null=True)),
                ('EditedOn', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]
