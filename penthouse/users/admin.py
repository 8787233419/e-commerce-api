from django.contrib import admin
from .models import Member
from .models import userlogin
from .models import pwd_history
from .models import Category
from .models import product
from .models import order

# Register your models here.
admin.site.register(Member)
admin.site.register(userlogin)
admin.site.register(pwd_history)
admin.site.register(Category)
admin.site.register(product)
admin.site.register(order)