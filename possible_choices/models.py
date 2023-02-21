from django.db import models

# Create your models here.


class MaterialChoices(models.Model):
    material = models.CharField(verbose_name='Материал', max_length=50)

    class Meta:
        verbose_name = 'Возможный материал'
        verbose_name_plural = 'Возможные материалы'

    def __str__(self):
        return self.material
