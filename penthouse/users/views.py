from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth.views import LoginView

class Login(LoginView) :
    template_name = 'users/profile.html'
    fields = '__all__'
    redirect_authenticated_user = True

def Home(request) :
    return HttpResponse("The main page")