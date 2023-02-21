# Generated by Django 3.2.17 on 2023-02-21 16:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('items_window', '0023_auto_20230221_1622'),
    ]

    operations = [
        migrations.AlterField(
            model_name='item',
            name='item_type',
            field=models.CharField(choices=[('flat', 'Квартира'), ('house', 'Дом'), ('land', 'Участок'), ('garage', 'Гараж'), ('carplace', 'Машиноместо'), ('com', 'Коммерческая недвижимость')], max_length=50, verbose_name='Тип объекта'),
        ),
        migrations.AlterField(
            model_name='item',
            name='type',
            field=models.CharField(choices=[('rent', 'Сдам'), ('sell', 'Продам'), ('buy', 'Куплю'), ('take', 'Сниму')], max_length=15, verbose_name='Тип объявления'),
        ),
    ]
