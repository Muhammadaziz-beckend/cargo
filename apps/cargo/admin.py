from django.contrib import admin

from .models import Trek, Store


@admin.register(Trek)
class TrekAdmin(admin.ModelAdmin):
    list_display = (
        "id",
        "number_trek",
        "owner",
        "china",
        "store",
        "client",
        "is_archived",
    )
    list_display_links = (
        "id",
        "number_trek",
        "owner",
        "china",
        "store",
        "client",
        "is_archived",
    )
    list_filter = (
        "china",
        "store",
        "client",
        "owner",
    )
    readonly_fields = ("store_user","is_archived",)


@admin.register(Store)
class StoreAdmin(admin.ModelAdmin):
    list_display = (
        "id",
        "name",
    )
    list_display_links = (
        "id",
        "name",
    )


# Register your models here.
