# Generated by Django 3.2.7 on 2021-09-24 21:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0009_devname_desc'),
    ]

    operations = [
        migrations.AlterField(
            model_name='devname',
            name='desc',
            field=models.TextField(default=''),
        ),
    ]