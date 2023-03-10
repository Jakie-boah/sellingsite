from django.db import models
from items_window.models import Item
from users.models import UserProfile
from django.core.exceptions import ObjectDoesNotExist
from phonenumber_field.modelfields import PhoneNumberField

# Create your models here.


class ReportChoices(models.Model):
    name = models.CharField(verbose_name='Причина', max_length=50)

    class Meta:
        verbose_name = 'Возможная причина репорта'
        verbose_name_plural = 'Возможные причины репортов'

    def __str__(self):
        return str(self.name)


class BlackList(models.Model):

    phone_number = PhoneNumberField(verbose_name='Номер телефона', region='RU')

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
        permissions = (
            ('control_black_list', 'Контролирует черный список'),
        )


class Report(models.Model):
    user = models.ForeignKey(UserProfile, default=None, on_delete=models.CASCADE, verbose_name='От:')
    item = models.ForeignKey(Item, default=None, on_delete=models.CASCADE, verbose_name='Объявление', blank=True, null=True)
    reason = models.ForeignKey(ReportChoices, on_delete=models.CASCADE, verbose_name='Причина', blank=True, null=True)
    report_text = models.TextField(verbose_name='Текст', blank=True, null=True)

    def __str__(self):
        return str(self.item)

    class Meta:
        verbose_name = 'Жалоба'
        verbose_name_plural = 'Жалобы'
        permissions = (
            ('control_reports', 'Контролирует жалобы'),
        )


class FeedBack(models.Model):

    phone_number = PhoneNumberField(region='RU', max_length=12, verbose_name='Номер телефона')
    email = models.EmailField(verbose_name="Почта")
    text = models.TextField(verbose_name='Сообщение')

    def __str__(self):
        return f'Обратная связь от {self.phone_number}'

    class Meta:
        verbose_name = 'Обратная связь'
        verbose_name_plural = 'Обратная связь'


