from django.db import models # type: ignore

# Create your models here.
class WareHouse(models.Model):
    name = models.CharField(max_length=100, unique=True)
    code = models.CharField(max_length=20, unique=True)
    address = models.CharField(max_length=255, blank=True)
    is_active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.code} - {self.name}"
    

class Product(models.Model):
    # usiamo lo SKU come chiave primaria, quindi niente "id" auto
    sku = models.CharField(max_length=64, primary_key=True)
    description = models.CharField(max_length=255)
    estimated_value = models.DecimalField(max_digits=10, decimal_places=2)
    weight = models.DecimalField(max_digits=10, decimal_places=3)
    pallet_quantity = models.PositiveIntegerField()

    def __str__(self):
        return f"{self.sku} - {self.description}"
    

class EanCode(models.Model):
    product = models.ForeignKey(
        Product,
        on_delete=models.CASCADE,
        related_name="ean_codes",
    )
    ean_code = models.CharField(max_length=64, unique=True)

    def __str__(self):
        return self.ean_code
    

class Location(models.Model):
    warehouse = models.ForeignKey(
        WareHouse,
        on_delete=models.CASCADE,
        related_name="locations",
    )
    name = models.CharField(max_length=50)  # es. '1A2P3' o 'TERRA'
    available = models.BooleanField(default=True)

    class Meta:
        unique_together = ("warehouse", "name")

    def __str__(self):
        return f"{self.warehouse.code} - {self.name}"
    
class InventoryItem(models.Model):
    warehouse = models.ForeignKey(
        WareHouse,
        on_delete=models.CASCADE,
        related_name="inventory_items",
    )
    location = models.ForeignKey(
        Location,
        on_delete=models.PROTECT,
        related_name="inventory_items",
    )
    product = models.ForeignKey(
        Product,
        on_delete=models.PROTECT,
        related_name="inventory_items",
    )
    quantity = models.PositiveIntegerField()

    class Meta:
        unique_together = ("warehouse", "location", "product")

    def __str__(self):
        return f"{self.product.sku} @ {self.location.name} ({self.quantity})"
