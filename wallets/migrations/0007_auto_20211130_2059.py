# Generated by Django 2.2.13 on 2021-11-30 20:59

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('wallets', '0006_auto_20210818_1241'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='beneficiary',
            name='bene_id',
        ),
        migrations.RemoveField(
            model_name='beneficiary',
            name='mobile_number',
        ),
        migrations.RemoveField(
            model_name='beneficiary',
            name='vpa',
        ),
    ]
