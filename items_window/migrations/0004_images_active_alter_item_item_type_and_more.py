# Generated by Django 4.1.5 on 2023-01-26 11:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('items_window', '0003_alter_item_street'),
    ]

    operations = [
        migrations.AddField(
            model_name='images',
            name='active',
            field=models.BooleanField(blank=True, default=False, editable=False, null=True),
        ),
        migrations.AlterField(
            model_name='item',
            name='item_type',
            field=models.CharField(choices=[('flat', 'Квартира'), ('house', 'Дом'), ('land', 'Участок'), ('garage', 'Гараж'), ('carplace', 'Машиноместо'), ('com', 'Коммерческая недвижимость')], max_length=50, verbose_name='Тип объекта'),
        ),
        migrations.AlterField(
            model_name='item',
            name='livin_surface',
            field=models.IntegerField(blank=True, null=True, verbose_name='Площадь жилая'),
        ),
        migrations.AlterField(
            model_name='item',
            name='type',
            field=models.CharField(choices=[('Сдам', 'Сдам'), ('Продам', 'Продам'), ('Куплю', 'Куплю'), ('Сниму', 'Сниму')], max_length=15, verbose_name='Тип'),
        ),
    ]
