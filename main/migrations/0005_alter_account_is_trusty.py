# Generated by Django 4.0.6 on 2022-11-19 18:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0004_alter_account_options_alter_account_managers_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='account',
            name='is_trusty',
            field=models.BooleanField(default=True, verbose_name='trusty'),
        ),
    ]
