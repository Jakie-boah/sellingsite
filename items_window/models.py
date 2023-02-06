from django.db import models
from phonenumber_field.modelfields import PhoneNumberField
from .handler import *
from decimal import Decimal
from geodata.models import Region
from django.core.validators import MinValueValidator


class Item(models.Model):

    type = models.CharField(max_length=15, choices=type_choices, verbose_name='Тип')
    item_type = models.CharField(max_length=50, choices=item_type_choices, verbose_name='Тип объекта')
    phone_number = PhoneNumberField(region='RU', verbose_name='Номер телефона')
    region = models.ForeignKey(Region, on_delete=models.PROTECT, verbose_name='Регион')
    city = models.CharField(verbose_name='Город', max_length=50)
    street = models.CharField(verbose_name='Улица', max_length=50)
    floor = models.IntegerField(verbose_name='Этаж', null=True, blank=True,
                                validators=[MinValueValidator(Decimal('0'))])
    total_floors = models.IntegerField(verbose_name='Этажей всего', null=True, blank=True,
                                       validators=[MinValueValidator(Decimal('0'))])
    material = models.CharField(verbose_name='Материал стен', choices=material_choices, max_length=100)
    total_surface = models.FloatField(verbose_name='Площадь общая', null=True, blank=True,
                                        validators=[MinValueValidator(Decimal('0.0'))])
    livin_surface = models.FloatField(verbose_name='Площадь жилая', null=True, blank=True,
                                        validators=[MinValueValidator(Decimal('0.0'))])
    price = models.IntegerField(verbose_name='Стоимость', null=True, blank=True,
                                validators=[MinValueValidator(Decimal('0'))])
    trade = models.BooleanField(verbose_name='Возможность обмена', default=False)
    description = models.TextField(verbose_name='Описание', null=True, blank=True)
    public = models.BooleanField(verbose_name='Опубликовать?', default=False, null=True, blank=True)
    banned = models.BooleanField(verbose_name='Заблокирован', default=False, null=True, blank=True, editable=False)

    def __str__(self):
        return str(self.pk)

    class Meta:
        verbose_name = 'Объявление'
        verbose_name_plural = 'Объявления'


class Images(models.Model):
    post = models.ForeignKey(Item, default=None, on_delete=models.PROTECT)
    image = models.ImageField(upload_to='items_img/',
                              verbose_name='Image')
    active = models.BooleanField(editable=False, default=False, blank=True, null=True)

    def __str__(self):
        return str(self.post)

    class Meta:
        verbose_name = 'Изображение'
        verbose_name_plural = 'Изображения'


class Comments(models.Model):
    post = models.ForeignKey(Item, default=None, on_delete=models.PROTECT)
    username = models.CharField(verbose_name='Имя', max_length=25, blank=True, null=True)
    text = models.TextField(verbose_name='Текст комментария', blank=True, null=True)

    def __str__(self):
        return str(self.post)

    class Meta:
        verbose_name = 'Комментарий'
        verbose_name_plural = 'Комментарии'



