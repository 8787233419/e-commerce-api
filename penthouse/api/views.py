from django.shortcuts import render
from rest_framework.decorators import api_view
from django.core.exceptions import ObjectDoesNotExist
from django.http import JsonResponse
from users.models import Category, Product, Order, Member
from .serializers import CategorySerializer, ProductSerializer, OrderSerializer, MemberSerializer, RegisterSerializer
from rest_framework import status 


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
    userDetails = Member.objects.filter(user_id = pk)
    serializer = MemberSerializer(userDetails)
    return JsonResponse(serializer.data, safe = False)

@api_view(['POST'])
def Login(request) :
    user_id = request.data.get('user_id')
    password = request.data.get('password')
    
    try :
        member = Member.objects.get(user_id = user_id)
        if member.password == password :
            serializer = MemberSerializer(member)
            return JsonResponse(serializer.data)
        else :
            return JsonResponse({'error': 'Incorrect password'})
    except ObjectDoesNotExist:
        return JsonResponse({'error': 'User does not exist'}, status=status.HTTP_400_BAD_REQUEST)


@api_view(['POST'])
def Register(request) :
    r_data={
        "user_id":request.data.get('user_id'),
        "full_name":request.data.get('full_name'),
        "address":request.data.get('address'),
        "mobile_no":request.data.get('mobile_no'),
        "password":request.data.get('password')
    }
    serializer = RegisterSerializer(data = r_data)

    if serializer.is_valid():
        member = serializer.save()  
        return JsonResponse({"message": "Member registered successfully","user_id": member.user_id}, status=status.HTTP_201_CREATED)
    
    return JsonResponse(serializer.errors, status=status.HTTP_400_BAD_REQUEST)