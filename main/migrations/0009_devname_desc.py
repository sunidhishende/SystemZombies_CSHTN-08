# Generated by Django 3.2.7 on 2021-09-24 21:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0008_auto_20210924_1946'),
    ]

    operations = [
        migrations.AddField(
            model_name='devname',
            name='desc',
            field=models.TextField(default='1'),
        ),
    ]
