from django.urls import path
from .views import CategoryList, ProductList, ProductByCategory, OrderByUser, Login, UserDetails

urlpatterns = [
    path('categories/', CategoryList, name='categorylist'),
    path('products/', ProductList, name='productlist'),
    path('productsbycategory/<str:pk>', ProductByCategory, name='productbycategory'),
    path('ordersbyuser/', OrderByUser, name='orderbyuser'),
    path('user-details/<str:pk>', UserDetails, name='user-details'),
    path('login/', Login, name='login'),
]