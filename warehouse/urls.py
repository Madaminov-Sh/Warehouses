from django.urls import path

from warehouse.views import ProductsListsAPIView

urlpatterns = [
    path('', ProductsListsAPIView.as_view())
]
