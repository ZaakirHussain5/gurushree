# Generated by Django 3.0.5 on 2020-12-18 11:06

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('transactions', '0008_auto_20201218_1557'),
    ]

    operations = [
        migrations.AddField(
            model_name='billheader',
            name='patient',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='transactions.patient_registration'),
        ),
    ]
