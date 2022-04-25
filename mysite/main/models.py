from django.db import models

# Create your models here.

class Mobile(models.Model):
    title = models.CharField('Модель', max_length=50)
    task = models.TextField('Описание')


    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Телефон'
        verbose_name_plural = 'Телефоны'
