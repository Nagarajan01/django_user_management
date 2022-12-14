from django.contrib.auth import authenticate, login, logout
from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from django.shortcuts import get_object_or_404
from django.db.models import Sum
from django.db.models import Count, F, Value, Q


from rest_framework import status, viewsets
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import generics


import json


from .utils import get_tokens_for_user
# from .serializers import RegistrationSerializer, PasswordChangeSerializer, UserSerializer, ProductSerializer, CartSerializer, ProductListSerializer, WishlistSerializer
# from .models import MyUser, Item, CartItem, Wishlist, Order
from .serializers import RegistrationSerializer, PasswordChangeSerializer, UserSerializer
from .models import MyUser
class RegistrationView(APIView):
    def post(self, request):
        a = request.data
        serializer = RegistrationSerializer(data=a)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class LoginView(APIView):
    def post(self, request):
        a = request.data
        print(request.data)
        if 'username' not in a or 'password' not in a:
            return Response({'msg': 'Credentials missing'}, status=status.HTTP_400_BAD_REQUEST)
        username = a['username']
        password = a['password']
        user = authenticate(request, username=username, password=password)
        print(request.data)
        if user is not None:
            login(request, user)
            auth_data = get_tokens_for_user(user)
            return Response({'msg': 'Login Success', **auth_data}, status=status.HTTP_200_OK)
        return Response({'msg': 'Invalid Credentials'}, status=status.HTTP_401_UNAUTHORIZED)


class LogoutView(APIView):
    def post(self, request):
        logout(request)
        return Response({'msg': 'Successfully Logged out'}, status=status.HTTP_200_OK)


class ChangePasswordView(APIView):
    permission_classes = [IsAuthenticated, ]

    def put(self, request):
        # pass posted data as parameters to PasswordChangeSerializer functions
        serializer = PasswordChangeSerializer(
            context={'request': request}, data=request.data.dict())
        # check serializer is valid or not
        serializer.is_valid(raise_exception=True)
        # if valid means new password will update password
        request.user.set_password(serializer.validated_data['new_password'])
        request.user.save()
        return Response({'msg': 'Password Successfully Updated'}, status=status.HTTP_200_OK)


class UserList(viewsets.ModelViewSet):              # >>> List of users
    permission_classes = [IsAuthenticated, ]
    queryset = MyUser.objects.all()
    serializer_class = UserSerializer


# class Product_List(viewsets.ModelViewSet):          # >>> List of products & add product to cart
#     permission_classes = [IsAuthenticated, ] 

#     queryset = Item.objects.all()
#     serializer_class = ProductListSerializer

#     def post(self, request, *args, **kwargs):
#         items = get_object_or_404(Item, id=self.kwargs.get('pk'))
#         if items.discount_price < items.price:
#             ncart = CartItem.objects.create(user=request.user, product=items)
#             ncart.total = ncart.quantity * items.discount_price
#             ncart.save()
#         else:
#             ncart = CartItem.objects.create(user=request.user, product=items)
#             ncart.total = ncart.quantity * items.price
#             ncart.save()
#         data = json.dumps(ncart, default=str, indent=1)
#         return Response({'msg': 'Product Added to Cart Successfully'}, status=status.HTTP_200_OK)


# class Cart(viewsets.ModelViewSet):                  # >>> List of Cart( get method ) & delete product from cart
#     permission_classes = [IsAuthenticated, ]
#     queryset = CartItem.objects.all()
#     serializer_class = CartSerializer
#     http_method_names = ['get', 'delete']

#     def get_queryset(self):
#         return CartItem.objects.filter(user=self.request.user)
#     def destroy(self, request, *args, **kwargs):
#         instance = self.get_object()
#         instance.delete()
#         return Response({"message": "Item deleted successfully"})


    
# class View_Wishlist(viewsets.ModelViewSet):
#     permission_classes = [IsAuthenticated, ] 
#     queryset = Wishlist.objects.all()
#     serializer_class = WishlistSerializer

    
#     def get(self):
#         return Wishlist.objects.filter(user=self.request.user)

#     def destroy(self, request, *args, **kwargs):
#         instance = self.get_object()
#         instance.delete()
#         return Response({"message": "Item deleted in Wishlist successfully"})
    
#     def post(self, request, *args, **kwargs):
#         query = Item.objects.get(id=kwargs['pk'])
#         print(query)
#         created = Wishlist.objects.get_or_create(user=request.user, wished_item=query)
#         return Response({"message": "Item added to wishlist successfully"})














# # class AddtoCartItemView(generics.ListCreateAPIView):  # >>> Add to cart method
# #     permission_classes = [IsAuthenticated, ] 
# #     queryset = CartItem.objects.all()

# #     serializer_class = CartSerializer

# #     def post(self, request, pk):
# #         query = Item.objects.get(id=pk, in_stock=True)
# #         items = get_object_or_404(Item, id=self.kwargs.get('pk'))
# #         print(items.price, items.discount_price)
# #         if items.discount_price < items.price:
# #             ncart = CartItem.objects.create(user=request.user, product=items)
# #             ncart.total = ncart.quantity * items.discount_price
# #             ncart.save()
# #         else:
# #             ncart = CartItem.objects.create(user=request.user, product=items)
# #             ncart.total = ncart.quantity * items.price
# #             ncart.save()
# #         data = json.dumps(ncart, default=str, indent=1)
# #         return Response({'msg': 'Product Added to Cart Successfully'}, status=status.HTTP_200_OK)
    
    



# # class Add_To_Wishlist(generics.ListCreateAPIView):
# #     permission_classes = [IsAuthenticated, ] 
# #     serializer_class = WishlistSerializer
# #     queryset = Wishlist.objects.all()

# #     def post(self, request, *args, **kwargs):
# #         query = Item.objects.get(id=kwargs['pk'])
# #         created = Wishlist.objects.get_or_create(user=request.user, wished_item=query)
# #         return Response({"message": "Item added to wishlist successfully"})