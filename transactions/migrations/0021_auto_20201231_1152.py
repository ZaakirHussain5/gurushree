# Generated by Django 3.0.5 on 2020-12-31 06:22

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('masters', '0006_auto_20201231_1136'),
        ('transactions', '0020_auto_20201231_1136'),
    ]

    operations = [
        migrations.AlterField(
            model_name='billdetails',
            name='SerDept',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='masters.service'),
        ),
    ]
