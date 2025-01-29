from django.urls import path
from .views import CategoryList, ProductList, ProductByCategory, OrderByUser

urlpatterns = [
    path('categories/', CategoryList, name='categorylist'),
    path('products/', ProductList, name='productlist'),
    path('productsbycategory/', ProductByCategory, name='productbycategory'),
    path('ordersbyuser/', OrderByUser, name='orderbyuser'),
]