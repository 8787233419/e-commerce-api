from django.urls import path
from .views import Register, Login, Logout
from django.contrib.auth.views import LogoutView

urlpatterns = [
    # path('', Home, name='home'),
    path('login/', Login , name = 'login'),
    path('register/', Register, name = 'register'),
    path('logout/', Logout, name = 'logout'),
]