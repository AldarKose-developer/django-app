# Generated by Django 4.0.1 on 2022-01-22 15:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hackhaton', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='adress',
            name='lat',
            field=models.CharField(max_length=30, null=True),
        ),
        migrations.AddField(
            model_name='adress',
            name='lng',
            field=models.CharField(max_length=30, null=True),
        ),
        migrations.AlterField(
            model_name='adress',
            name='cadNumber',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='adress',
            name='home',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
    ]
