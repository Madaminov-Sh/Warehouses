from rest_framework import generics

from warehouse.serializers import ProductSerializer
from warehouse.models import Product


class ProductsListsAPIView(generics.ListAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer