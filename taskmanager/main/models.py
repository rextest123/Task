from django.db import models
from django import forms
from django.contrib.auth.models import User
# Create your models here.

class Task(models.Model):
    title = models.CharField('Название', max_length=50)
    task = models.TextField('Описание')
    ready = models.BooleanField(default=False)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Заявки'
        verbose_name_plural = 'Заявки'


class Items(models.Model):
    title = models.CharField('Название', max_length=50)
    price = models.TextField("Цена")
    description = models.TextField("Описание")
    actors = models.TextField("Актеры")
    image = models.ImageField(upload_to='images')

    def __str__(self):
        return self.title


    class Meta:
        verbose_name = 'Мероприятие'
        verbose_name_plural = 'Мероприятия'

class Docs(models.Model):
    title = models.CharField('Название', max_length=50)
    description = models.TextField("Описание")
    doc = models.FileField(upload_to='specs')

    def __str__(self):
        return self.title


    class Meta:
        verbose_name = 'Документ'
        verbose_name_plural = 'Документы'

class Tasks(models.Model):
    title = models.CharField('Название', max_length=50)
    deadline = models.TextField("Срок выполнения")
    description = models.TextField("Описание")
    person = models.TextField("Ответственный")
    ready = models.BooleanField(default=False)

    def __str__(self):
        return self.title


    class Meta:
        verbose_name = 'Поручение'
        verbose_name_plural = 'Поручения'