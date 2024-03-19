from rest_framework import serializers

from warehouse.models import Product, Material, ProductMaterials, Warehouses


class ProductMaterialSerializer(serializers.ModelSerializer):
    material_name = serializers.StringRelatedField(source='material.title')

    class Meta:
        model = ProductMaterials
        fields = ('warehouse', 'material_name', 'quantity', 'price')


class ProductSerializer(serializers.ModelSerializer):
    materials = ProductMaterialSerializer(many=True)

    class Meta:
        model = Product
        fields = ('id', 'title', 'code', 'materials')
