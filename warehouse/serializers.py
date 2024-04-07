from rest_framework import serializers

from warehouse.models import Product, Material, ProductMaterials, Warehouses


class ProductMaterialSerializer(serializers.ModelSerializer):
    material_name = serializers.StringRelatedField(source='material.title')
    price = serializers.SerializerMethodField('get_materials_prices')

    class Meta:
        model = ProductMaterials
        fields = ('warehouse', 'material_name', 'quantity', 'price')

    def get_materials_prices(self, obj):
        if obj.warehouse and obj.warehouse.price_per_material > 0:
            try:
                return int(obj.warehouse.price_per_material) * int(obj.quantity)
            except:
                return False
        return None


class ProductSerializer(serializers.ModelSerializer):
    productmaterials = ProductMaterialSerializer(many=True)

    class Meta:
        model = Product
        fields = ('id', 'title', 'code', 'productmaterials')
