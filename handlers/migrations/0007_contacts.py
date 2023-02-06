# Generated by Django 3.2.17 on 2023-02-05 12:35

from django.db import migrations, models
import phonenumber_field.modelfields


class Migration(migrations.Migration):

    dependencies = [
        ('handlers', '0006_report_user'),
    ]

    operations = [
        migrations.CreateModel(
            name='Contacts',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('phone_number', phonenumber_field.modelfields.PhoneNumberField(blank=True, max_length=12, null=True, region='RU', verbose_name='Номер телефона')),
                ('email', models.EmailField(blank=True, max_length=254, null=True, verbose_name='Почта')),
                ('telegram', models.CharField(blank=True, max_length=50, null=True, verbose_name='Телеграм')),
                ('vk', models.CharField(blank=True, max_length=50, null=True, verbose_name='Вконтакте')),
                ('insta', models.CharField(blank=True, max_length=50, null=True, verbose_name='Инстаграм')),
            ],
            options={
                'verbose_name': 'Контакты',
                'verbose_name_plural': 'Контакты',
            },
        ),
    ]