from django.db import models
from django import forms
from django.contrib.auth.models import User
# Create your models here.

class Task(models.Model):
    title = models.CharField('Название', max_length=50)
    task = models.TextField('Описание')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Задача'
        verbose_name_plural = 'Задачи'


class Items(models.Model):
    title = models.CharField('Название', max_length=50)
    price = models.TextField("Цена")
    image = models.ImageField(upload_to='images')

    def __str__(self):
        return self.title


    class Meta:
        verbose_name = 'Товар'
        verbose_name_plural = 'Товары'

