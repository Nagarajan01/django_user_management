from rest_framework import serializers
from .models import MyUser, Item, Brand, CartItem, Order


class RegistrationSerializer(serializers.ModelSerializer):
    password2 = serializers.CharField(style={"input_type": "password"}, write_only=True)

    class Meta:
        model = MyUser
        fields = ['email', 'date_of_birth', 'password', 'password2']
        extra_kwargs = {
            'password': {'write_only': True}
        }

    def save(self):
        user = MyUser(email=self.validated_data['email'], date_of_birth=self.validated_data['date_of_birth'])
        password = self.validated_data['password']
        password2 = self.validated_data['password2']
        if password != password2:
            raise serializers.ValidationError({'password': 'Passwords must match.'})
        user.set_password(password)
        user.save()
        return user

class PasswordChangeSerializer(serializers.Serializer):
    current_password = serializers.CharField(style={"input_type": "password"}, required=True)
    new_password = serializers.CharField(style={"input_type": "password"}, required=True)

    def validate_current_password(self, value):
        if not self.context['request'].user.check_password(value):
            raise serializers.ValidationError({'current_password': 'Does not match'})
        return value

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = MyUser
        fields = ('email', 'id', 'password', 'date_of_birth')
        read_only_fields = ('id',)
        extra_kwargs = {
            'password': {'write_only': True}
        }

class BrandSerializer(serializers.ModelSerializer):
    class Meta:
        model = Brand
        fields = ('id', 'brand', 'brand_image', 'is_active')

class ProductSerializer(serializers.HyperlinkedModelSerializer):
    brand = BrandSerializer(many=True, read_only=True)

    class Meta:
        model = Item
        fields = ['id', 'title', 'brand', 'price', 'discount_price', 'image']

class CartSerializer(serializers.ModelSerializer):
    product = ProductSerializer(read_only=True)
    user = UserSerializer(read_only=True)

    class Meta: 
        model = CartItem
        fields = ['id', 'user', 'created_at', 'product', 'quantity', 'total', 'ordered']
        extra_kwargs = {
        }
