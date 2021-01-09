# Generated by Django 3.0.5 on 2020-12-24 10:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('transactions', '0018_auto_20201224_1603'),
    ]

    operations = [
        migrations.AlterField(
            model_name='billdetails',
            name='Balance',
            field=models.DecimalField(decimal_places=2, max_digits=50, null=True),
        ),
        migrations.AlterField(
            model_name='billdetails',
            name='HospDisc',
            field=models.DecimalField(decimal_places=2, max_digits=50, null=True),
        ),
        migrations.AlterField(
            model_name='billdetails',
            name='HospShare',
            field=models.DecimalField(decimal_places=2, max_digits=50, null=True),
        ),
        migrations.AlterField(
            model_name='billdetails',
            name='ReferDisc',
            field=models.DecimalField(decimal_places=2, max_digits=50, null=True),
        ),
        migrations.AlterField(
            model_name='billdetails',
            name='ReferShare',
            field=models.DecimalField(decimal_places=2, max_digits=50, null=True),
        ),
        migrations.AlterField(
            model_name='billheader',
            name='Advance',
            field=models.DecimalField(decimal_places=2, max_digits=50, null=True),
        ),
        migrations.AlterField(
            model_name='billheader',
            name='Balance',
            field=models.DecimalField(decimal_places=2, max_digits=100, null=True),
        ),
        migrations.AlterField(
            model_name='billheader',
            name='DiscPerc',
            field=models.DecimalField(decimal_places=2, max_digits=50, null=True),
        ),
        migrations.AlterField(
            model_name='billheader',
            name='DrDiscount',
            field=models.DecimalField(decimal_places=2, max_digits=50, null=True),
        ),
        migrations.AlterField(
            model_name='billheader',
            name='HospDiscount',
            field=models.DecimalField(decimal_places=2, max_digits=50, null=True),
        ),
        migrations.AlterField(
            model_name='billheader',
            name='NetAmount',
            field=models.DecimalField(decimal_places=2, max_digits=100, null=True),
        ),
        migrations.AlterField(
            model_name='billheader',
            name='PaidAmount',
            field=models.DecimalField(decimal_places=2, max_digits=100, null=True),
        ),
        migrations.AlterField(
            model_name='billheader',
            name='Payable',
            field=models.DecimalField(decimal_places=2, max_digits=100, null=True),
        ),
        migrations.AlterField(
            model_name='billheader',
            name='ReferDiscount',
            field=models.DecimalField(decimal_places=2, max_digits=50, null=True),
        ),
        migrations.AlterField(
            model_name='billheader',
            name='TPABalance',
            field=models.DecimalField(decimal_places=2, max_digits=50, null=True),
        ),
        migrations.AlterField(
            model_name='billheader',
            name='TobeRefund',
            field=models.DecimalField(decimal_places=2, max_digits=50, null=True),
        ),
        migrations.AlterField(
            model_name='billheader',
            name='TotalAmount',
            field=models.DecimalField(decimal_places=2, max_digits=50, null=True),
        ),
        migrations.AlterField(
            model_name='billheader',
            name='TotalDiscount',
            field=models.DecimalField(decimal_places=2, max_digits=50, null=True),
        ),
        migrations.AlterField(
            model_name='billreceipt',
            name='Card',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=50, null=True),
        ),
        migrations.AlterField(
            model_name='billreceipt',
            name='CardTotal',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=50, null=True),
        ),
        migrations.AlterField(
            model_name='billreceipt',
            name='Cash',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=50, null=True),
        ),
        migrations.AlterField(
            model_name='billreceipt',
            name='OtherPaid',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=50, null=True),
        ),
        migrations.AlterField(
            model_name='billreceipt',
            name='Transfee',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=50, null=True),
        ),
    ]