from . import models
from django.contrib import admin


@admin.action(description='Включить')
def turn_on_active(modeladmin, request, queryset):
    queryset.update(active=True)


@admin.action(description='Выключить')
def turn_off_active(modeladmin, request, queryset):
    queryset.update(active=False)


@admin.register(models.Schema)
class SchemaAdmin(admin.ModelAdmin):
    fields = ('name', 'schema_id')
    list_display = ('name', 'schema_id')
    search_fields = ('name', 'schema_id')


@admin.register(models.DeviceGroup)
class DeviceGroupAdmin(admin.ModelAdmin):
    list_display = ('name', 'active')
    search_fields = ('name',)
    list_filter = ('active',)
    actions = (turn_on_active, turn_off_active)


@admin.register(models.Device)
class DeviceAdmin(admin.ModelAdmin):
    fieldsets = (
        ('Информация о машине', {'fields': ('name', 'device_id', 'active')}),
        ('Дополнительная информация', {'fields': ('group', 'schema')})
    )
    list_display = ('name', 'device_id', 'active')
    search_fields = ('name', 'device_id')
    list_filter = ('group', 'schema', 'active')
    actions = (turn_on_active, turn_off_active)


