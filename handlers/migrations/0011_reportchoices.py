# Generated by Django 3.2.17 on 2023-02-21 16:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('handlers', '0010_alter_report_options'),
    ]

    operations = [
        migrations.CreateModel(
            name='ReportChoices',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, verbose_name='Причина')),
            ],
            options={
                'verbose_name': 'Возможная причина репорта',
                'verbose_name_plural': 'Возможные причины репортов',
            },
        ),
    ]
