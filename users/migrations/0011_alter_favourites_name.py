# Generated by Django 3.2.17 on 2023-03-14 11:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0010_alter_favourites_name'),
    ]

    operations = [
        migrations.AlterField(
            model_name='favourites',
            name='name',
            field=models.TextField(blank=True, default='Охарактеризуйте тип этого объявления', null=True, verbose_name='Название'),
        ),
    ]
