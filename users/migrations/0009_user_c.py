# Generated by Django 2.2.2 on 2021-07-20 06:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0008_auto_20210709_1355'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='c',
            field=models.IntegerField(default=0),
        ),
    ]