from rest_framework import serializers
from users.models import Category, Product, Order, Member

class CategorySerializer(serializers.ModelSerializer) :
    class Meta :
        model = Category
        fields = '__all__'

class ProductSerializer(serializers.ModelSerializer):
    class Meta :
        model = Product
        fields = '__all__'

class OrderSerializer(serializers.ModelSerializer):
    class Meta :
        model = Order
        fields = '__all__'

class MemberSerializer(serializers.ModelSerializer):
    class Meta :
        model = Member
        fields = '__all__'

class RegisterSerializer(serializers.ModelSerializer):
    class Meta :
        model = Member
        fields = ['user_id', 'full_name', 'address', 'mobile_no', 'password']