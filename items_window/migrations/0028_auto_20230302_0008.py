# Generated by Django 3.2.17 on 2023-03-02 00:08

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('items_window', '0027_auto_20230301_1736'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='images',
            name='index_store',
        ),
        migrations.RemoveField(
            model_name='images',
            name='index_store_2',
        ),
        migrations.RemoveField(
            model_name='images',
            name='index_store_3',
        ),
    ]
