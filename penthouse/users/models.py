from django.db import models
from django.core.validators import MaxLengthValidator, MinLengthValidator

# Create your models here.
# pw boolfor admin --- remaining
class Member(models.Model) :
    user_id = models.CharField(max_length = 50)
    full_name = models.CharField(max_length = 200)
    address = models.CharField(max_length = 500)
    mobile_no = models.IntegerField(max_length=10)
    password = models.CharField(max_length = 16, validators = [MinLengthValidator(8)])

    def __str__(self) :
        return self.user_id

