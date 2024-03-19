from django.urls import path

from warehouse import views

urlpatterns = [
    path('', views.ProductAPIView.as_view())
]