from django.contrib import admin

# Register your models here.
from .models import WareHouse, EanCode, Product, Location, InventoryItem


@admin.register(WareHouse)
class WarehouseAdmin(admin.ModelAdmin):
    list_display = ("id", "code", "name", "is_active", "created_at")
    search_fields = ("code", "name")
    list_filter = ("is_active",)


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ("sku", "description", "estimated_value", "weight", "pallet_quantity")
    search_fields = ("sku", "description")


@admin.register(EanCode)
class EanCodeAdmin(admin.ModelAdmin):
    list_display = ("ean_code", "product")
    search_fields = ("ean_code", "product__sku")

@admin.register(Location)
class LocationAdmin(admin.ModelAdmin):
    list_display = ("id", "warehouse", "name", "available")
    search_fields = ("name", "warehouse__code")
    list_filter = ("warehouse", "available")


@admin.register(InventoryItem)
class InventoryItemAdmin(admin.ModelAdmin):
    list_display = ("id", "warehouse", "location", "product", "quantity")
    search_fields = ("product__sku", "location__name", "warehouse__code")
    list_filter = ("warehouse", "location")