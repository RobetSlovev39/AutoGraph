from django.db import models


class Schema(models.Model):
    ''' Модель схемы ( на случай если будет больше одной ) '''

    schema_id = models.CharField('ID', max_length=50, unique=True)
    name = models.CharField('Название', max_length=150)

    def __str__(self) -> str:
        return self.name

    class Meta:
        verbose_name = 'Схему'
        verbose_name_plural = 'Схемы'


class DeviceGroup(models.Model):
    ''' Модель групп машин, которые будут отображаться на карте '''

    name = models.CharField(
        'Название группы',
        max_length=50,
        help_text='Имя группы, машины которой будут обрабатываться'
    )

    active = models.BooleanField('Включено', default=True, help_text='Показывается ли группа машин на карте')

    schema = models.ForeignKey(
        Schema,
        on_delete=models.CASCADE,
        verbose_name='Схема',
        related_name='device_groups',
    )

    def __str__(self) -> str:
        return self.name

    class Meta:
        verbose_name = 'Группу машин'
        verbose_name_plural = 'Группы машин'


class Device(models.Model):
    ''' Модель машины '''

    name = models.CharField('Название', max_length=50)
    device_id = models.CharField('ID', max_length=50, unique=True)
    active = models.BooleanField('Включено', default=True, help_text='Показывается ли машина на карте')

    group = models.ForeignKey(
        DeviceGroup,
        on_delete=models.CASCADE,
        verbose_name='Группа',
        related_name='devices'
    )

    def __str__(self) -> str:
        return self.name

    class Meta:
        verbose_name = 'Машину'
        verbose_name_plural = 'Машины'


class GeofenceGroup(models.Model):
    ''' Модель групп геозон, которые будут отображаться на карте '''

    name = models.CharField(
        'Название группы',
        max_length=50,
        help_text='Имя группы, геозоны которой будут обрабатываться'
    )

    active = models.BooleanField('Включено', default=True, help_text='Показывается ли группа геозон на карте')

    schema = models.ForeignKey(
        Schema,
        on_delete=models.CASCADE,
        verbose_name='Схема',
        related_name='geofence_groups'
    )

    def __str__(self) -> str:
        return self.name

    class Meta:
        verbose_name = 'Группу геозон'
        verbose_name_plural = 'Группы геозон'


class Geofence(models.Model):
    ''' Модель геозоны '''

    name = models.CharField('Название', max_length=50)
    geofence_id = models.CharField('ID', max_length=50, unique=True)
    active = models.BooleanField('Включено', default=True, help_text='Показывается ли геозона на карте')

    group = models.ForeignKey(
        GeofenceGroup,
        on_delete=models.CASCADE,
        verbose_name='Группа',
        related_name='geofences'
    )

    def __str__(self) -> str:
        return self.name

    class Meta:
        verbose_name = 'Геозону'
        verbose_name_plural = 'Геозоны'
