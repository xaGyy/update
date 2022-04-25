from django.contrib.auth.models import AbstractUser
from django.db import models

class User(AbstractUser):
    pass

class Mobile(models.Model):
    title = models.CharField('Модель', max_length=50)
    task = models.TextField('Описание')


    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Телефон'
        verbose_name_plural = 'Телефоны'
