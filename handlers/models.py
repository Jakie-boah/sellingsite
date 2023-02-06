from django.db import models
from items_window.models import Item
from users.models import UserProfile
from django.core.exceptions import ObjectDoesNotExist
from phonenumber_field.modelfields import PhoneNumberField

# Create your models here.


class BlackList(models.Model):

    phone_number = PhoneNumberField(verbose_name='Номер телефона')

    def __str__(self):
        return str(self.phone_number)

    def __init__(self, *args, **kwargs):
        super(BlackList, self).__init__(*args, **kwargs)

        try:
            for item in Item.objects.filter(phone_number=self.phone_number).all():
                item.banned = True
                item.save()

        except ObjectDoesNotExist:
            pass

    class Meta:
        verbose_name = 'Черный список'
        verbose_name_plural = 'Черный список'


class Report(models.Model):
    user = models.ForeignKey(UserProfile, default=None, on_delete=models.PROTECT, verbose_name='От:')
    item = models.ForeignKey(Item, default=None, on_delete=models.PROTECT, verbose_name='Объявление')
    report_text = models.TextField(verbose_name='Текст')

    def __str__(self):
        return str(self.item)

    class Meta:
        verbose_name = 'Жалоба'
        verbose_name_plural = 'Жалобы'


class Contacts(models.Model):

    phone_number = PhoneNumberField(region='RU', max_length=12, verbose_name='Номер телефона', blank=True, null=True)
    email = models.EmailField(verbose_name="Почта", blank=True, null=True)
    telegram = models.CharField(max_length=50, verbose_name='Телеграм', blank=True, null=True)
    vk = models.CharField(max_length=50, verbose_name='Вконтакте', blank=True, null=True)
    insta = models.CharField(max_length=50, verbose_name='Инстаграм', blank=True, null=True)

    class Meta:
        verbose_name = 'Контакты'
        verbose_name_plural = 'Контакты'
