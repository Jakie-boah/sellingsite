from django.db import models
from phonenumber_field.modelfields import PhoneNumberField
from .handler import *
from geodata.models import Region, SubRegion
from possible_choices.models import *


class Item(models.Model):
    date = models.DateField(auto_now_add=True, blank=True, null=True, verbose_name='Дата')
    type = models.CharField(max_length=15, choices=type_choices, verbose_name='Тип объявления')
    item_type = models.CharField(max_length=50, choices=item_type_choices, verbose_name='Тип объекта')
    phone_number = PhoneNumberField(region='RU', verbose_name='Номер телефона')
    region = models.ForeignKey(Region, on_delete=models.CASCADE, verbose_name='Регион')
    sub_region = models.ForeignKey(SubRegion, on_delete=models.CASCADE, verbose_name='Район', blank=True, null=True)
    city = models.CharField(verbose_name='Город', max_length=50)
    street = models.CharField(verbose_name='Улица', max_length=50)
    floor = models.IntegerField(verbose_name='Этаж', null=True, blank=True)
    total_floors = models.IntegerField(verbose_name='Этажей всего', null=True, blank=True)
    material = models.ForeignKey(MaterialChoices, on_delete=models.CASCADE, verbose_name='Материал стен', null=True, blank=True)
    total_surface = models.FloatField(verbose_name='Площадь общая', null=True, blank=True)
    livin_surface = models.FloatField(verbose_name='Площадь жилая', null=True, blank=True)
    price = models.IntegerField(verbose_name='Стоимость', null=True, blank=True)
    trade = models.BooleanField(verbose_name='Возможность обмена', default=False)
    name = models.CharField(verbose_name='Основное название', max_length=100, blank=True, null=True)
    description = models.TextField(verbose_name='Описание', null=True, blank=True)
    public = models.BooleanField(verbose_name='Опубликовать?', default=False, null=True, blank=True)
    banned = models.BooleanField(verbose_name='Заблокирован', default=False, null=True, blank=True, editable=False)
    no_pictures = models.BooleanField(verbose_name='Объявление без фотографий', default=False, null=True, blank=True, editable=False)

    def __str__(self):
        return str(self.pk)

    class Meta:
        verbose_name = 'Объявление'
        verbose_name_plural = 'Объявления'
        permissions = (
            ('can_change_item', "Может изменять объявление"),
            ('can_delete_item', "Может удалить объявление"),
            ('control_new_items', 'Контролирует новые объявления'),
        )


class Images(models.Model):
    url_height = models.PositiveIntegerField(default=560, blank=True, null=True)
    url_width = models.PositiveIntegerField(default=400, blank=True, null=True)
    post = models.ForeignKey(Item, default=None, on_delete=models.CASCADE)
    image = models.ImageField(upload_to='items_img/',
                              verbose_name='Image', height_field='url_height', width_field='url_width')

    active = models.BooleanField(editable=False, default=False, blank=True, null=True)

    def __str__(self):
        return str(self.post)

    class Meta:
        verbose_name = 'Изображение'
        verbose_name_plural = 'Изображения'






