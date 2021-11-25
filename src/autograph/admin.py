from . import models
from django.contrib import admin


@admin.register(models.Schema)
class SchemaAdmin(admin.ModelAdmin):
    pass
