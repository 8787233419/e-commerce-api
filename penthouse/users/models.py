from itertools import product
from django.db import models
from django.core.validators import MaxLengthValidator, MinLengthValidator

# Create your models here.
# pw boolfor admin --- remaining

#create models regarding userid, userlogin, password history and other data regarding users
class Member(models.Model) :
    user_id = models.CharField(max_length = 50)
    full_name = models.CharField(max_length = 200)
    address = models.CharField(max_length = 500)
    mobile_no = models.IntegerField()
    password = models.CharField(max_length = 16, validators = [MinLengthValidator(8)])

    def __str__(self) :
        return self.user_id

class userlogin(models.Model) :
    user_id = models.CharField(max_length = 50)
    full_name = models.CharField(max_length = 200)
    password = models.CharField(max_length = 16, validators = [MinLengthValidator(8)])

    def __str__(self) :
        return self.full_name


class pwd_history(models.Model):
    user_id=models.IntegerField()
    creation_date = models.DateTimeField()
    password= models.CharField(max_length = 16, validators = [MinLengthValidator(8)])

    def __str__(self):
        return self.user_id
    
#models for products, their categories, pricing, history etc
    
class Category(models.Model):
    cat_id=models.IntegerField(unique=True)
    cat_name = models.CharField(max_length=255, unique=True)
    desc= models.CharField(max_length=500)

    def __str__(self):
        return self.cat_name
    
class product(models.Model):
    cat_id=models.IntegerField(unique=True)
    cat_name = models.CharField(max_length=255, unique=True)
    prod_id=models.IntegerField(unique=True)
    prod_name=models.CharField(max_length=255)
    prod_desc=models.CharField(max_length=500)
    price=models.IntegerField()
    stock_qty=models.IntegerField()

    def __str__(self):
        return self.prod_name
    
#models for order,payment,orderlist,shipping etc
class order(models.Model):
    prod_id=models.IntegerField(unique=True)
    prod_name=models.CharField(max_length=255)
    price=models.IntegerField()
    qty=models.IntegerField()
    order_id=models.IntegerField()

    def __str__(self):
        return self.order_id


    

    

    

    



