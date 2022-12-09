# Generated by Django 4.0.6 on 2022-12-03 13:51

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0005_alter_account_is_trusty'),
    ]

    operations = [
        migrations.CreateModel(
            name='SocialAccount',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('login', models.CharField(max_length=200, verbose_name='login')),
                ('password', models.CharField(max_length=500, verbose_name='Password')),
                ('social_network', models.CharField(max_length=100, verbose_name='Network')),
                ('account', models.ManyToManyField(to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'ordering': ['social_network'],
            },
        ),
    ]