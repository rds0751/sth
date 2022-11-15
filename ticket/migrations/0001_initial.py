# Generated by Django 2.2.2 on 2021-07-01 08:36

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Priority',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=32)),
                ('value', models.IntegerField()),
                ('is_default', models.BooleanField(default=False)),
                ('display_color', models.TextField(default='#000000', max_length=16)),
            ],
        ),
        migrations.CreateModel(
            name='Project',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=32)),
                ('is_default', models.BooleanField(default=False)),
            ],
        ),
        migrations.CreateModel(
            name='Status',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=32)),
                ('is_default', models.BooleanField(default=False)),
                ('hide_by_default', models.BooleanField(default=False)),
            ],
        ),
        migrations.CreateModel(
            name='Ticket',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=128)),
                ('desc', models.TextField()),
                ('ss', models.FileField(null=True, upload_to='support/')),
                ('creation_time', models.DateTimeField()),
                ('update_time', models.DateTimeField()),
                ('time_logged', models.FloatField(default=0)),
            ],
        ),
        migrations.CreateModel(
            name='TicketComment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text', models.TextField()),
                ('ss', models.FileField(null=True, upload_to='support/')),
                ('update_time', models.DateTimeField()),
                ('time_logged', models.FloatField(default=0)),
                ('automated', models.BooleanField(default=False)),
            ],
        ),
    ]