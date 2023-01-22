from django.db import models
from phonenumber_field.modelfields import PhoneNumberField

# Create your models here.


class BlackList(models.Model):
    phone_number = PhoneNumberField(unique=True, verbose_name='Номер телефона')

    class Meta:
        verbose_name = 'Черный список'
        verbose_name_plural = 'Черный список'

