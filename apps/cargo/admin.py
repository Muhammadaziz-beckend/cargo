from django.contrib import admin

from .models import Trek, Warehouse


@admin.register(Trek)
class TrekAdmin(admin.ModelAdmin):
    list_display = (
        "id",
        "number_trek",
        "owner",
        "status",
    )
    list_display_links = (
        "id",
        "number_trek",
        "owner",
    )
    list_filter = (
        "status",
        "owner",
    )
    list_editable = ("status",)


@admin.register(Warehouse)
class WarehouseAdmin(admin.ModelAdmin):
    list_display = (
        "id",
        "name",
    )
    list_display_links = (
        "id",
        "name",
    )
    

# Register your models here.
