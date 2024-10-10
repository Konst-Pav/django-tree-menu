from django.db import models


class Menu(models.Model):
    objects = models.Manager
    name = models.CharField(max_length=100)
    parent = models.ForeignKey('self', on_delete=models.CASCADE, null=True, blank=True)
    slug = models.SlugField(max_length=100, unique=True, verbose_name='slug')

    class Meta:
        verbose_name = 'Пункт меню'
        verbose_name_plural = 'Пункт меню'

    def __str__(self):
        return self.name
