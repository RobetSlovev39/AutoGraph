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
    list_display = ('name', 'active', 'schema')
    search_fields = ('name',)
    list_filter = ('active',)
    actions = (turn_on_active, turn_off_active)


@admin.register(models.Device)
class DeviceAdmin(admin.ModelAdmin):
    fieldsets = (
        ('Информация о машине', {'fields': ('name', 'device_id')}),
        ('Дополнительная информация', {'fields': ('group', 'active')})
    )
    list_display = ('name', 'device_id', 'active')
    search_fields = ('name', 'device_id')
    list_filter = ('group', 'active')
    actions = (turn_on_active, turn_off_active)


@admin.register(models.GeofenceGroup)
class GeofenceGroupAdmin(admin.ModelAdmin):
    list_display = ('name', 'active', 'schema')
    search_fields = ('name',)
    list_filter = ('active',)
    actions = (turn_on_active, turn_off_active)


@admin.register(models.Geofence)
class GeofenceAdmin(admin.ModelAdmin):
    fieldsets = (
        ('Информация о геозоне', {'fields': ('name', 'geofence_id')}),
        ('Дополнительная информация', {'fields': ('group', 'active')})
    )
    list_display = ('name', 'geofence_id', 'active')
    search_fields = ('name', 'geofence_id')
    list_filter = ('group', 'active')
    actions = (turn_on_active, turn_off_active)
