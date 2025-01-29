from django.shortcuts import render
from rest_framework.decorators import api_view
from django.http import JsonResponse
from users.models import Category, Product
from .serializers import CategorySerializer, ProductSerializer

@api_view(['GET'])
def CategoryList(request) :
    categories = Category.objects.all()
    serializer = CategorySerializer(categories, many = True)
    return JsonResponse(serializer.data, safe = False)

@api_view(['GET'])
def ProductList(request) :
    products = Product.objects.all()
    serializer = ProductSerializer(products, many = True)
    return JsonResponse(serializer.data, safe = False)

@api_view(['GET'])
def ProductByCategory(request) :
    category = request.query_params.get('category') # .data for POST

    products = Product.objects.filter(category = category) # .get expects 1 object
    serializer = ProductSerializer(products, many = True)
    return JsonResponse(serializer.data, safe = False)


# login, logout, register, all prev order/cart, user details