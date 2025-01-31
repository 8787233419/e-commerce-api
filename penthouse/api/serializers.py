from rest_framework import serializers
from users.models import Category, Product, Order, Member
from django.core.validators import MinLengthValidator, MinValueValidator, MaxValueValidator

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
        fields = 'user_id','full_name','address','mobile_no'

class RegisterSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True, min_length=8, max_length=16, validators=[MinLengthValidator(8)])

    class Meta:
        model = Member
        fields = ['user_id', 'full_name', 'address', 'mobile_no', 'password']

    def create(self, validated_data):
        member = Member.objects.create(
            user_id=validated_data['user_id'],
            full_name=validated_data['full_name'],
            address=validated_data['address'],
            mobile_no=validated_data['mobile_no']
        )
        member.password = validated_data['password']
        member.save()
        return member