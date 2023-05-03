from django.urls import path
from products.views import products, index

app_name = 'products'

urlpatterns = [
    path('products/', products, name='products'),
    path('', index, name='index'),
    ]
