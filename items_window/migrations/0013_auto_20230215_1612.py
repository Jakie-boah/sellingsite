# Generated by Django 3.2.17 on 2023-02-15 16:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('items_window', '0012_alter_item_type'),
    ]

    operations = [
        migrations.AddField(
            model_name='item',
            name='date',
            field=models.DateField(auto_now_add=True, null=True, verbose_name='Дата'),
        ),
        migrations.AddField(
            model_name='item',
            name='name',
            field=models.CharField(blank=True, max_length=100, null=True, verbose_name='Основное название'),
        ),
        migrations.AlterField(
            model_name='item',
            name='floor',
            field=models.IntegerField(blank=True, null=True, verbose_name='Этаж'),
        ),
        migrations.AlterField(
            model_name='item',
            name='livin_surface',
            field=models.FloatField(blank=True, null=True, verbose_name='Площадь жилая'),
        ),
        migrations.AlterField(
            model_name='item',
            name='price',
            field=models.IntegerField(blank=True, null=True, verbose_name='Стоимость'),
        ),
        migrations.AlterField(
            model_name='item',
            name='total_floors',
            field=models.IntegerField(blank=True, null=True, verbose_name='Этажей всего'),
        ),
        migrations.AlterField(
            model_name='item',
            name='total_surface',
            field=models.FloatField(blank=True, null=True, verbose_name='Площадь общая'),
        ),
    ]
