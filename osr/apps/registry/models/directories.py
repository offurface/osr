from django.db import models
from .objects import *
from django.urls import reverse


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


class Rank(models.Model):
    name = models.CharField(max_length=250, verbose_name="Наименование разряда")
    rank = models.PositiveIntegerField(verbose_name="Разряд")

    def __str__(self):
        return "%s %s" % (self.name, self.rank)

    class Meta:
        ordering = ("name", "rank",)
        verbose_name = "Разряд"
        verbose_name_plural = "Разряд"


