from django.db import models
from users.models import UserProfile
from geodata.models import Region
# Create your models here.


class AdminsRegions(models.Model):
    admin = models.OneToOneField(UserProfile, verbose_name='Админ', on_delete=models.CASCADE)
    region = models.ManyToManyField(Region, verbose_name='Регион/ы')

    def __str__(self):
        return f'Админ {self.admin.username} в регионе {self.region}'

    class Meta:
        verbose_name = 'Админы по регионам'
        verbose_name_plural = 'Админы по регионам'


