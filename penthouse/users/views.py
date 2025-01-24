from django.shortcuts import render
from rest_framework import viewsets
from .models import Member, UserLogin, PwdHistory, Category, Product, Order
from .serializer import MemberSerializer #, UserLogin, PwdHistory, Category, Product, Order

def getMember(request) :
    queryset = Member.objects.all()
    serializer = MemberSerializer
    # return Response(serializer.data)

# class Login(LoginView) :
#     template_name = 'users/profile.html'
#     fields = '__all__'
#     redirect_authenticated_user = True

# def Home(request) :
#     return HttpResponse("The main page")