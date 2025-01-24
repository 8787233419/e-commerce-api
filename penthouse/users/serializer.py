from rest_framework import serializers
from .models import Member, UserLogin, PwdHistory, Category, Product, Order

class MemberSerializer(serializers.HyperlinkedModelSerializer) :
    class Meta:
        model = Member
        fields = ('user_id', 'full_name', 'address', 'mobile_no', 'password')

# class User