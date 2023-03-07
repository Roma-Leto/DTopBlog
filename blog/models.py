# -*- coding: utf-8 -*-
from django.db import models
from django.contrib.auth.models import AbstractUser
import datetime


class BUser(AbstractUser):
    is_activated = models.BooleanField(default=True, verbose_name='Прошёл активацию?')


    class Meta(AbstractUser.Meta):
        pass


class BNotePost(models.Model):
    data_publish = models.DateTimeField(auto_now_add=True, db_index=True, verbose_name="Дата")
    title = models.CharField(max_length=50, blank=False)
    article = models.CharField(max_length=200)
    #start_task = models.DateField(null=True, blank=True, auto_now=True,editable=True, verbose_name="начало")
    #fin_task = models.DateField(blank=True, null=True, verbose_name="окончание")
    user_post = models.ForeignKey(BUser, related_name='pk', on_delete=models.CASCADE) 
    

    class Meta:
        verbose_name_plural = 'Рубрики'
        verbose_name = 'Рубрика'
        ordering = ['data_publish']

