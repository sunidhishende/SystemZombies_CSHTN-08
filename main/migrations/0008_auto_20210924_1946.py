# Generated by Django 3.2.7 on 2021-09-24 14:16

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0007_auto_20210924_1749'),
    ]

    operations = [
        migrations.CreateModel(
            name='Question',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('question', models.CharField(max_length=300)),
                ('option1', models.CharField(max_length=300)),
                ('option2', models.CharField(max_length=300)),
                ('option3', models.CharField(max_length=300)),
                ('option4', models.CharField(max_length=300)),
                ('correct_option', models.IntegerField(validators=[django.core.validators.MaxValueValidator(4), django.core.validators.MinValueValidator(1)])),
            ],
        ),
        migrations.AddField(
            model_name='video',
            name='questions',
            field=models.ManyToManyField(to='main.Question'),
        ),
    ]
