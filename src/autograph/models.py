from django.db import models


class Schema(models.Model):
    schema_id = models.CharField('ID', max_length=50, unique=True)
    name = models.CharField('Название', max_length=150)

    def __str__(self) -> str:
        return self.name

    class Meta:
        verbose_name = 'схему'
        verbose_name_plural = 'схемы'


class DeviceGroup(models.Model):
    name = models.CharField('Имя группы',
    max_length=50,
    help_text='Имя группы, машины которой будут обрабатываться')

    def __str__(self) -> str:
        return self.name

    class Meta:
        verbose_name = 'Группу машин'
        verbose_name_plural = 'Группы машин'
