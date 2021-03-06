# Generated by Django 3.0.5 on 2021-01-04 09:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('transactions', '0026_auto_20210102_1831'),
    ]

    operations = [
        migrations.AlterField(
            model_name='prescriptionmedication',
            name='evening',
            field=models.DecimalField(decimal_places=2, default=0.0, max_digits=7),
        ),
        migrations.AlterField(
            model_name='prescriptionmedication',
            name='lunch',
            field=models.DecimalField(decimal_places=2, default=0.0, max_digits=7),
        ),
        migrations.AlterField(
            model_name='prescriptionmedication',
            name='morning',
            field=models.DecimalField(decimal_places=2, default=0.0, max_digits=7),
        ),
        migrations.AlterField(
            model_name='prescriptionmedication',
            name='night',
            field=models.DecimalField(decimal_places=2, default=0.0, max_digits=7),
        ),
        migrations.AlterField(
            model_name='prescriptionmedication',
            name='qty',
            field=models.DecimalField(decimal_places=2, default=0.0, max_digits=7),
        ),
    ]
