# Generated by Django 3.2.17 on 2023-03-01 17:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('items_window', '0025_item_no_pictures'),
    ]

    operations = [
        migrations.AlterField(
            model_name='images',
            name='image',
            field=models.ImageField(height_field='1077', upload_to='items_img/', verbose_name='Image', width_field='1600'),
        ),
    ]
