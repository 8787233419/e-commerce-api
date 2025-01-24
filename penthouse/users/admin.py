from django.contrib import admin
from .models import Member
from .models import UserLogin
from .models import PwdHistory
from .models import Category
from .models import Product
from .models import Order

# Register your models here.
admin.site.register(Member)
admin.site.register(UserLogin)
admin.site.register(PwdHistory)
admin.site.register(Category)
admin.site.register(Product)
admin.site.register(Order)