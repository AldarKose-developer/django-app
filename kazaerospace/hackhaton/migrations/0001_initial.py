# Generated by Django 4.0.1 on 2022-01-22 10:19

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Adress',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('firstname', models.CharField(max_length=100)),
                ('lastname', models.CharField(max_length=100)),
                ('middleName', models.CharField(blank=True, max_length=100, null=True)),
                ('iin', models.CharField(max_length=12)),
                ('city', models.CharField(max_length=100)),
                ('street', models.CharField(max_length=100)),
                ('home', models.CharField(max_length=100)),
                ('homeNumber', models.CharField(blank=True, max_length=100, null=True)),
                ('cadNumber', models.CharField(max_length=100)),
                ('area', models.CharField(blank=True, max_length=100, null=True)),
                ('info', models.CharField(blank=True, max_length=500, null=True)),
            ],
        ),
    ]
