from django.contrib import admin

from warehouse.models import Product, ProductMaterials, Material, Warehouses


admin.site.register(Product)
admin.site.register(ProductMaterials)
admin.site.register(Material)
admin.site.register(Warehouses)
