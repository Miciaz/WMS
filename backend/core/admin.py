from django.contrib import admin

# Register your models here.
from .models import WareHouse


@admin.register(WareHouse)
class WarehouseAdmin(admin.ModelAdmin):
    list_display = ("id", "code", "name", "is_active", "created_at")
    search_fields = ("code", "name")
    list_filter = ("is_active",)
