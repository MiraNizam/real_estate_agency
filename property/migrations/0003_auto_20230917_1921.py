# Generated by Django 2.2.24 on 2023-09-17 16:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('property', '0002_auto_20230917_1920'),
    ]

    operations = [
        migrations.AlterField(
            model_name='flat',
            name='new_building',
            field=models.BooleanField(blank=True, default=None, null=True, verbose_name='Новостройка'),
        ),
    ]
