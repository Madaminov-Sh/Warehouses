import uuid

from django.db import models


class BaseModel(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True


class Product(BaseModel):
    title = models.CharField(max_length=255)
    code = models.UUIDField(unique=True, default=uuid.uuid4, editable=False)

    def __str__(self):
        return self.title

    class Meta:
        db_table = 'product'
        verbose_name = 'Product'
        verbose_name_plural = 'Products'


class Material(BaseModel):
    title = models.CharField(max_length=255, unique=True)

    def __str__(self):
        return self.title

    class Meta:
        db_table = 'material'
        verbose_name = 'Material'
        verbose_name_plural = 'Materials'


class ProductMaterials(BaseModel):
    warehouse = models.ForeignKey('Warehouses', on_delete=models.CASCADE, related_name='productmaterials', null=True,
                                  blank=True)
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='productmaterials')
    material = models.ForeignKey(Material, on_delete=models.CASCADE, related_name='productmaterials')

    quantity = models.IntegerField(help_text='foydalaniladigan xomashyolar soni.')

    def __str__(self):
        return f"{self.product} - {self.material}"

    class Meta:
        db_table = 'product_material'
        verbose_name = 'ProductMaterial'
        verbose_name_plural = 'ProductMaterials'

    def check_subtract_quantity_remainder(self):
        if self.warehouse_id:
            warehouse = self.warehouse
            warehouse.remainder -= self.quantity
            warehouse.save()

    def check_warehouse_none(self):
        if self.warehouse_id and self.warehouse.remainder <= 0:
            self.warehouse = None

    def save(self, *args, **kwargs):
        self.check_subtract_quantity_remainder()
        self.check_warehouse_none()
        super().save(*args, **kwargs)


class Warehouses(BaseModel):
    material = models.ForeignKey(Material, on_delete=models.CASCADE, related_name='warehouses')

    remainder = models.IntegerField(help_text='ushbu partiyadan nechta xomashyo qolganini ko’rsatadi.')
    price = models.IntegerField(help_text='ushbu partiyada kelgan mahsulot qanday narxda kelganini ko’rsatadi.')
    price_per_material = models.IntegerField(help_text="qo'shilgan har bir dona maxsulot narxi.", blank=True, null=True)

    def __str__(self):
        return f"{self.id} - partiya, {self.material}"

    class Meta:
        db_table = 'warehouse'
        verbose_name = 'Warehouse'
        verbose_name_plural = 'Warehouses'

    def check_price_per_material(self):
        self.price_per_material = self.price / self.remainder

    def save(self, *args, **kwargs):
        self.check_price_per_material()
        super().save(*args, **kwargs)
