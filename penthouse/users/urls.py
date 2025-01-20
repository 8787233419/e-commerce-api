from django.urls import path
from .views import Login, Home
from django.contrib.auth.views import LogoutView

urlpatterns = [
    path('', Home, name='home'),
    path('login/', Login.as_view(), name='login'),
    path('logout/', LogoutView.as_view(next_page='login'), name='logout'),
]