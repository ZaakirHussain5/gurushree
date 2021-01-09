# Generated by Django 3.0.5 on 2021-01-01 06:18

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('transactions', '0023_auto_20201231_1259'),
    ]

    operations = [
        migrations.CreateModel(
            name='PrescriptionHeader',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('height', models.DecimalField(decimal_places=2, default=0.0, max_digits=6)),
                ('weight', models.DecimalField(decimal_places=3, default=0.0, max_digits=7)),
                ('bmi', models.DecimalField(decimal_places=2, default=0.0, max_digits=7)),
                ('pulse_rate', models.DecimalField(decimal_places=2, default=0.0, max_digits=7)),
                ('body_temparature', models.DecimalField(decimal_places=2, default=0.0, max_digits=7)),
                ('blood_pressure', models.DecimalField(decimal_places=2, default=0.0, max_digits=7)),
                ('respiraty_rate', models.DecimalField(decimal_places=2, default=0.0, max_digits=7)),
                ('pallor', models.BooleanField(default=False)),
                ('Icterus', models.BooleanField(default=False)),
                ('systemic_examinations', models.CharField(blank=True, max_length=100, null=True)),
                ('complaints_and_duration', models.TextField(blank=True, null=True)),
                ('history_and_comorbidities', models.TextField(blank=True, null=True)),
                ('provisional_diagnosis', models.TextField(blank=True, null=True)),
                ('investigation_details', models.TextField(blank=True, null=True)),
                ('review_date', models.DateTimeField()),
                ('bill_header', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='transactions.billheader')),
            ],
        ),
        migrations.CreateModel(
            name='PrescriptionMedication',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('particular_name', models.CharField(blank=True, max_length=100, null=True)),
                ('morning', models.IntegerField(default=0)),
                ('lunch', models.IntegerField(default=0)),
                ('evening', models.IntegerField(default=0)),
                ('night', models.IntegerField(default=0)),
                ('days', models.IntegerField(default=1)),
                ('qty', models.IntegerField(default=0)),
                ('advice', models.CharField(blank=True, max_length=500, null=True)),
                ('bill_header', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='transactions.billheader')),
                ('prescription_header', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='transactions.PrescriptionHeader')),
            ],
        ),
    ]
