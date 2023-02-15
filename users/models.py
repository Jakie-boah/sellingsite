from django.contrib.auth.models import AbstractUser
from django.db import models
from phonenumber_field.modelfields import PhoneNumberField
from items_window.models import Item
# Create your models here.


class UserProfile(AbstractUser):
    phone_number = PhoneNumberField(unique=True, verbose_name='Номер телефона')
    username = models.CharField(verbose_name='Имя', max_length=50)
    usersurname = models.CharField(verbose_name='Фамилия', max_length=50)
    email = models.EmailField(unique=True, verbose_name='Почта')
    password = models.CharField(verbose_name='Пароль', max_length=100, blank=True, null=True)
    blocked = models.BooleanField(verbose_name='Заблокирован', default=False, blank=True, null=True)

    USERNAME_FIELD = 'phone_number'
    REQUIRED_FIELDS = ['username', 'email']

    def __str__(self):
        return str(self.phone_number)

    class Meta:
        verbose_name = 'Пользователь'
        verbose_name_plural = 'Пользователи'


class Favourites(models.Model):
    user = models.ForeignKey(UserProfile, on_delete=models.CASCADE, verbose_name='Пользователь')
    item = models.ForeignKey(Item, on_delete=models.PROTECT, verbose_name='Объявление')

    def __str__(self):
        return str(self.item)

    class Meta:
        verbose_name = 'Избранное'
        verbose_name_plural = 'Избранное'


class Comments(models.Model):
    post = models.ForeignKey(Item, default=None, on_delete=models.CASCADE, verbose_name='Объявление')
    user = models.ForeignKey(UserProfile, default=None, on_delete=models.CASCADE, verbose_name='Пользователь')
    text = models.TextField(verbose_name='Текст комментария', blank=True, null=True)

    def __str__(self):
        return str(self.post)

    class Meta:
        verbose_name = 'Комментарий'
        verbose_name_plural = 'Комментарии'