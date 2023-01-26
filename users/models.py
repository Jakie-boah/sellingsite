from django.contrib.auth.models import AbstractUser
from django.db import models
from phonenumber_field.modelfields import PhoneNumberField

# Create your models here.


class UserProfile(AbstractUser):
    phone_number = PhoneNumberField(unique=True, verbose_name='Номер телефона')
    username = models.CharField(verbose_name='Имя', max_length=50)
    usersurname = models.CharField(verbose_name='Фамилия', max_length=50)
    email = models.EmailField(unique=True, verbose_name='Почта')
    password = models.CharField(verbose_name='Пароль', max_length=100, blank=True, null=True)

    USERNAME_FIELD = 'phone_number'
    REQUIRED_FIELDS = ['username', 'email']

    def __str__(self):
        return self.username

    class Meta:
        verbose_name = 'Пользователь'
        verbose_name_plural = 'Пользователи'



