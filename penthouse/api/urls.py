from django.urls import path
from .views import CategoryList, ProductList, ProductByCategory

urlpatterns = [
    path('categories/', CategoryList, name='categorylist'),
    path('products/', ProductList, name='productlist'),
    path('productsbycategory/', ProductByCategory, name='productbycategory'),
]