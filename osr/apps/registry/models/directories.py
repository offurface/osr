from django.db import models
from .objects import *
from django.urls import reverse

class Physique(models.Model):
    height = models.DecimalField(max_digits=4, decimal_places=1, verbose_name="Рост")
    weight = models.DecimalField(max_digits=4, decimal_places=1, verbose_name="Вес")
    body_type = models.CharField(max_length=150, verbose_name="Тип тела")

    def __str__(self):
        return "%s" % self.id

    class Meta:
        ordering = ("body_type",)
        verbose_name = "Телосложение отца и матери"
        verbose_name_plural = "Телосложение отца и матери"


class Sport_type(models.Model):
    name = models.CharField(max_length=250, verbose_name="Наименование")

    def __str__(self):
        return self.name
    def get_absolute_url(self,*args,**kwargs):
        return reverse('sport-type-detail', kwargs={'pk': self.pk})
    class Meta:
        ordering = ("name",)
        verbose_name = "Вид спорта"
        verbose_name_plural = "Виды спорта"


class Previous_sport(models.Model):
    name = models.CharField(max_length=250, verbose_name="Наименование")
    years = models.PositiveIntegerField(verbose_name="Лет")
    months = models.PositiveIntegerField(verbose_name="Месяцев")
    rank = models.PositiveIntegerField(verbose_name="Разряд")

    def __str__(self):
        return self.name

    class Meta:
        ordering = ("name",)
        verbose_name = "Предыдущий вид спорта"
        verbose_name_plural = "Предыдущий вид спорта"


