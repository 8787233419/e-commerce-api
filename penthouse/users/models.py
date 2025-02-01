from itertools import product
from django.db import models
from django.core.validators import MaxValueValidator , MinValueValidator,MinLengthValidator

# Create your models here.
# pw boolfor admin --- remaining

#create models regarding userid, userlogin, password history and other data regarding users
class Member(models.Model) :
    user_id = models.CharField(primary_key=True,max_length = 50)
    full_name = models.CharField(max_length = 200)
    address = models.CharField(max_length = 500)
    mobile_no = models.IntegerField( validators = [MinValueValidator(6666666666),MaxValueValidator(9999999999)])
    password = models.CharField(max_length = 16, validators = [MinLengthValidator(8)])

    def __str__(self) :
        return self.user_id
'''
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
'''
#models for products, their categories, pricing, history etc
    
class Category(models.Model):
    cat_id = models.IntegerField(primary_key=True)
    cat_name = models.CharField(max_length=255)
    desc= models.CharField(max_length=500)
    cat_img = models.ImageField( upload_to = './images')

    def __str__(self):
        return self.cat_name
    def category_img(self):
        return self.cat_img
    
class Product(models.Model):
    category = models.ForeignKey(Category, on_delete = models.CASCADE, null = True)
    product_id = models.IntegerField(primary_key=True)
    product_name = models.CharField(max_length=255)
    product_desc = models.CharField(max_length=500)
    product_img = models.ImageField(upload_to = './images',null=True,blank=True)
    price = models.IntegerField()
    

    def __str__(self):
        return self.product_name
    

class Order(models.Model):
    product_id = models.ForeignKey(Product, on_delete = models.CASCADE, null = True)
    order_total = models.DecimalField(max_digits=10, decimal_places=2)
    order_date = models.DateTimeField(null=True,blank=True)
    order_id = models.CharField(primary_key=True,max_length=25)
    user_id=models.ForeignKey(Member,on_delete=models.CASCADE,null=True)
    address= models.CharField(max_length=500,default="no address provided")
    full_name= models.CharField(max_length=50,default="user123")
    mobile_no=models.IntegerField(validators=[MinValueValidator(6666666666),MaxValueValidator(9999999999)],null=True)

    def __str__(self):
        return self.order_id
    
      