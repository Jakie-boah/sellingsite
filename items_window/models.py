from django.db import models
from phonenumber_field.modelfields import PhoneNumberField
from .handler import *
from geodata.models import Region
from django.db.models import Q
#from cities_light.models import Region


# Create your models here.
class PostManager(models.Manager):
    def search(self, query=None):
        qs = self.get_queryset()
        if query is not None:
            or_lookup = (Q(type__icontains=query) |
                         Q(item_type__icontains=query) |
                         Q(city__icontains=query) |
                         Q(floor__icontains=query) |
                         Q(total_floors__icontains=query) |
                         Q(material__icontains=query) |
                         Q(total_surface__icontains=query) |
                         Q(livin_surface__icontains=query) |
                         Q(price__icontains=query) |
                         Q(trade__icontains=query) |
                         Q(description__icontains=query))
            qs = qs.filter(or_lookup).distinct()
        return qs


class Item(models.Model):

    type = models.CharField(max_length=15, choices=type_choices, verbose_name='Тип')
    item_type = models.CharField(max_length=50, choices=item_type_choices, verbose_name='Тип объекта')
    phone_number = PhoneNumberField()
    region = models.ForeignKey(Region, on_delete=models.PROTECT, verbose_name='Регион')
    city = models.CharField(verbose_name='Город', max_length=50)
    street = models.CharField(verbose_name='Улица', max_length=50)
    floor = models.IntegerField(verbose_name='Этаж', null=True, blank=True)
    total_floors = models.IntegerField(verbose_name='Этажей всего', null=True, blank=True)
    material = models.CharField(verbose_name='Материал стен', choices=material_choices, max_length=100)
    total_surface = models.IntegerField(verbose_name='Площадь общая', null=True, blank=True)
    livin_surface = models.IntegerField(verbose_name='Площадь жилая', null=True, blank=True)
    price = models.IntegerField(verbose_name='Стоимость', null=True, blank=True)
    trade = models.BooleanField(verbose_name='Возможность обмена', default=False)
    description = models.TextField(verbose_name='Описание', null=True, blank=True)
    public = models.BooleanField(verbose_name='Опубликовать?', default=False, null=True, blank=True)
    banned = models.BooleanField(verbose_name='Заблокирован', default=False, null=True, blank=True, editable=False)

    objects = PostManager()

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
