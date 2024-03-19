from rest_framework import generics

from warehouse import serializers
from warehouse.models import Product, ProductMaterials, Warehouses


class ProductAPIView(generics.ListAPIView):
    serializer_class = serializers.ProductSerializer
    queryset = Product.objects.all()
