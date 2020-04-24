
from django.urls import path
from .views import products,product,create_product,create_product_raw_form,create_product_raw_form_class

app_name="products"

urlpatterns = [
    path('', products, name='products'),
    path('<int:id>', product, name='product-details'),
    path('create',create_product , name='create'),
    path('create/raw',create_product_raw_form , name='create'),
    path('create/rawClass',create_product_raw_form_class , name='create')
]
