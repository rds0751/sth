# Generated by Django 2.2.13 on 2021-08-18 07:11

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('wallets', '0005_auto_20210716_1458'),
    ]

    operations = [
        migrations.CreateModel(
            name='MetatraderAccount',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user', models.CharField(max_length=20)),
                ('generated', models.NullBooleanField()),
                ('account', models.CharField(blank=True, max_length=20, null=True)),
                ('password', models.CharField(blank=True, max_length=10, null=True)),
                ('created_at', models.DateTimeField(blank=True, default=django.utils.timezone.now)),
                ('updated_at', models.DateTimeField(blank=True, default=django.utils.timezone.now)),
            ],
        ),
        migrations.DeleteModel(
            name='FundRequest',
        ),
    ]