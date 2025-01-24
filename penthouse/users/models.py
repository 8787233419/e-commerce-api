from itertools import product
from django.db import models
from django.core.validators import MaxValueValidator , MinValueValidator,MinLengthValidator

# Create your models here.
# pw boolfor admin --- remaining

#create models regarding userid, userlogin, password history and other data regarding users
class Member(models.Model) :
    user_id = models.CharField(max_length = 50)
    full_name = models.CharField(max_length = 200)
    address = models.CharField(max_length = 500)
    mobile_no = models.IntegerField( validators = [MinValueValidator(6666666666),MaxValueValidator(9999999999)])
    password = models.CharField(max_length = 16, validators = [MinLengthValidator(8)])

    def __str__(self) :
        return self.user_id

class UserLogin(models.Model) :
    user = models.OneToOneField(Member, on_delete = models.CASCADE, null = True)
    password = models.CharField(max_length = 16, validators = [MinLengthValidator(8)])

    def __str__(self) :
        return self.user.user_id


class PwdHistory(models.Model):
    user = models.ForeignKey(Member, on_delete = models.CASCADE, null = True)
    creation_date = models.DateTimeField()
    password= models.CharField(max_length = 16, validators = [MinLengthValidator(8)])

    def __str__(self):
        return self.user.user_id
    
#models for products, their categories, pricing, history etc
    
class Category(models.Model):
    cat_id = models.IntegerField(unique=True)
    cat_name = models.CharField(max_length=255, unique=True)
    desc= models.CharField(max_length=500)
    cat_img = models.ImageField( upload_to = './images', default = './images/template.png')

    def __str__(self):
        return self.cat_name
    def category_img(self):
        return self.cat_img
    
class Product(models.Model):
    category = models.ForeignKey(Category, on_delete = models.CASCADE, null = True)
    prod_id = models.IntegerField(unique=True)
    prod_name = models.CharField(max_length=255)
    prod_desc = models.CharField(max_length=500)
    product_img = models.ImageField(upload_to = './images', default = './images/template.png')
    price = models.IntegerField()
    stock_qty = models.IntegerField()

    def __str__(self):
        return self.prod_name
    
#models for order,payment,orderlist,shipping etc
class Order(models.Model):
    product = models.ForeignKey(Product, on_delete = models.CASCADE, null = True)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    qty = models.IntegerField()
    order_id = models.IntegerField()

    def __str__(self):
        return self.order_id