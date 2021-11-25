from . import models
from django.contrib import admin


@admin.register(models.Schema)
class SchemaAdmin(admin.ModelAdmin):
    fields = ('name', 'schema_id')


@admin.register(models.DeviceGroup)
class DeviceGroupAdmin(admin.ModelAdmin):
    pass
