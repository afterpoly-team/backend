# Generated by Django 3.1.7 on 2021-04-15 12:27

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0007_auto_20210415_1521'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='address',
            name='corps_en',
        ),
        migrations.RemoveField(
            model_name='address',
            name='corps_fr',
        ),
        migrations.RemoveField(
            model_name='address',
            name='corps_ru',
        ),
    ]