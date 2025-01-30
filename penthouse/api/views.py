from django.shortcuts import render
from rest_framework.decorators import api_view
from django.core.exceptions import ObjectDoesNotExist
from django.http import JsonResponse
from users.models import Category, Product, Order, Member
from .serializers import CategorySerializer, ProductSerializer, OrderSerializer, MemberSerializer

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
def ProductByCategory(request,pk) :
#     category = pk # .data for POST
#     print (category)
    products = Product.objects.filter(category = pk) # .get expects 1 object
    print(products)
    serializer = ProductSerializer(products, many = True)
    return JsonResponse(serializer.data, safe = False)

@api_view(['GET'])
def OrderByUser(request) :
    user = request.query_params.get('user_id')
    order = Order.objects.filter(user_id=user)
    serializer = OrderSerializer(order, many= True)
    return JsonResponse(serializer.data, safe= False )

@api_view(['GET'])
def UserDetails(request,pk) :
    # user_id =pk
    # print(user_id)
    userDetails = Member.objects.filter(user_id = pk)
    # print (userDetails.data)
    serializer = MemberSerializer(userDetails)
    return JsonResponse(serializer.data, safe = False)

@api_view(['POST'])
def Login(request) :
    user_id = request.data.get('user_id')
    password = request.data.get('password')
    
    try :
        member = Member.objects.get(user_id = user_id)
      #  print (member.user_id)
        if member.password == password :
            serializer = MemberSerializer(member)
            return JsonResponse(serializer.data)
        else :
            return JsonResponse({'error': 'Incorrect password'})
    except ObjectDoesNotExist:
        return JsonResponse({'error': 'User does not exist'})

# login, logout, register, all prev order/cart, user details