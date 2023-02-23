# Generated by Django 3.2.17 on 2023-02-20 10:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('geodata', '0001_initial'),
        ('advanced_admin', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='adminsregions',
            name='region',
        ),
        migrations.AddField(
            model_name='adminsregions',
            name='region',
            field=models.ManyToManyField(to='geodata.Region', verbose_name='Регион/ы'),
        ),
    ]