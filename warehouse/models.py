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


class Material(BaseModel):
    title = models.CharField(max_length=255)

    def __str__(self):
        return self.title


class ProductMaterials(BaseModel):
    warehouse = models.ForeignKey('Warehouses', on_delete=models.CASCADE, related_name='materials')
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='materials')
    material = models.ForeignKey(Material, on_delete=models.CASCADE, related_name='materials')

    quantity = models.IntegerField(help_text='foydalaniladigan xomashyolar soni.')
    price = models.IntegerField(help_text='Mahsulot ishlab chiqarishda ishlatiladigan xomashyo narxi.')

    def __str__(self):
        return f"{self.product} - {self.material}"


class Warehouses(BaseModel):
    material = models.ForeignKey(Material, on_delete=models.CASCADE, related_name='warehouses')

    quantity = models.IntegerField(help_text='ushbu partiyadan nechta xomashyo qolganini ko’rsatadi.')
    price = models.IntegerField(help_text='ushbu partiyada kelgan mahsulot qanday narxda kelganini ko’rsatadi.')

    def __str__(self):
        return f"{self.id} - partiya, {self.material}"
