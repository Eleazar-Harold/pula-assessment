from django.contrib import admin

from .models import Farm, Harvest, Resource


# Register your models here.
@admin.register(Farm)
class FarmAdmin(admin.ModelAdmin):
    list_display = [
        "name",
        "owner",
        "crop",
        "size",
        "town",
        "location",
        "created",
    ]
    list_filter = (
        "name",
        "size",
        "crop",
        "town",
        "owner__email",
    )


@admin.register(Harvest)
class HarvestAdmin(admin.ModelAdmin):
    list_display = [
        "farm",
        "harvest_weight",
        "dry_weight",
        "created",
    ]
    list_filter = (
        "farm__name",
        "harvest_weight",
        "dry_weight",
    )


@admin.register(Resource)
class ResourceAdmin(admin.ModelAdmin):
    pass
