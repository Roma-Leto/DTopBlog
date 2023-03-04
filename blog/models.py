# -*- coding: utf-8 -*-
from django.db import models
from django.contrib.auth.models import AbstractUser


class BUser(AbstractUser):
    is_activated = models.BooleanField(default=True, db_index=True, verbose_name='Прошёл активацию?')


    class Meta(AbstractUser.Meta):
        pass


class BNotePost(models.Model):
    data_publish = models.DateField(auto_now_add=True, verbose_name="Дата")
    title = models.CharField(max_length=50, blank=False)
    article = models.CharField(max_length=200)
    start_task = models.DateField(verbose_name="начало")
    fin_task = models.DateField(verbose_name="окончание")
    user_post = models.ForeignKey('BUser', on_delete=models.CASCADE) 

    class Meta:
        verbose_name_plural = 'Рубрики'
        verbose_name = 'Рубрика'
        ordering = ['data_publish']

