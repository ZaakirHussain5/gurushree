# Generated by Django 2.2.12 on 2020-06-15 02:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('masters', '0015_auto_20200614_1159'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='professional',
            name='deptId',
        ),
        migrations.AddField(
            model_name='professional',
            name='department',
            field=models.CharField(max_length=32, null=True),
        ),
        migrations.AlterField(
            model_name='hospital',
            name='hospitalName',
            field=models.CharField(max_length=100, null=True),
        ),
    ]
