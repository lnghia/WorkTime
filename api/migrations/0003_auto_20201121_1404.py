# Generated by Django 3.1.3 on 2020-11-21 14:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0002_auto_20201121_1255'),
    ]

    operations = [
        migrations.AlterField(
            model_name='worker',
            name='email',
            field=models.EmailField(max_length=254, unique=True),
        ),
    ]
