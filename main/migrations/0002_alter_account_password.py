# Generated by Django 4.0.6 on 2022-11-15 13:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='account',
            name='password',
            field=models.CharField(max_length=500, verbose_name='Password'),
        ),
    ]
