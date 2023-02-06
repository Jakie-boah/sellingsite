# Generated by Django 3.2.17 on 2023-02-05 12:35

from django.db import migrations
import phonenumber_field.modelfields


class Migration(migrations.Migration):

    dependencies = [
        ('items_window', '0010_alter_item_phone_number'),
    ]

    operations = [
        migrations.AlterField(
            model_name='item',
            name='phone_number',
            field=phonenumber_field.modelfields.PhoneNumberField(max_length=128, region='RU', verbose_name='Номер телефона'),
        ),
    ]