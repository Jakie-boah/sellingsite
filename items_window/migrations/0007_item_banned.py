# Generated by Django 4.1.5 on 2023-01-30 09:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('items_window', '0006_item_public'),
    ]

    operations = [
        migrations.AddField(
            model_name='item',
            name='banned',
            field=models.BooleanField(blank=True, default=False, editable=False, null=True, verbose_name='Заблокирован'),
        ),
    ]
