from rest_framework import generics, status
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from main.models import Banner, Category, Product, ProductImg, Cart, CartProduct, Order, ProductEnter, Info, WishList
from .serializers import (
    BannerSerializer, CategorySerializer, ProductSerializer, ProductImgSerializer, 
    CartSerializer, CartProductSerializer, OrderSerializer, ProductEnterSerializer, 
    InfoSerializer, WishListSerializer, UserSerializer
)

class BannerListCreateView(generics.ListCreateAPIView):
    queryset = Banner.objects.all()
    serializer_class = BannerSerializer

class BannerDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Banner.objects.all()
    serializer_class = BannerSerializer

class CategoryListCreateView(generics.ListCreateAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer

class CategoryDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer

class ProductListCreateView(generics.ListCreateAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

class ProductDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

class CartListCreateView(generics.ListCreateAPIView):
    queryset = Cart.objects.all()
    serializer_class = CartSerializer
    permission_classes = [IsAuthenticated]

class CartDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Cart.objects.all()
    serializer_class = CartSerializer
    permission_classes = [IsAuthenticated]

class CartProductListCreateView(generics.ListCreateAPIView):
    queryset = CartProduct.objects.all()
    serializer_class = CartProductSerializer

class CartProductDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = CartProduct.objects.all()
    serializer_class = CartProductSerializer

class OrderListCreateView(generics.ListCreateAPIView):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer

class OrderDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer

class ProductEnterListCreateView(generics.ListCreateAPIView):
    queryset = ProductEnter.objects.all()
    serializer_class = ProductEnterSerializer

class ProductEnterDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = ProductEnter.objects.all()
    serializer_class = ProductEnterSerializer

class InfoListCreateView(generics.ListCreateAPIView):
    queryset = Info.objects.all()
    serializer_class = InfoSerializer

class InfoDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Info.objects.all()
    serializer_class = InfoSerializer

class WishListListCreateView(generics.ListCreateAPIView):
    queryset = WishList.objects.all()
    serializer_class = WishListSerializer
    permission_classes = [IsAuthenticated]

class WishListDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = WishList.objects.all()
    serializer_class = WishListSerializer
    permission_classes = [IsAuthenticated]

class AddProductToCartView(APIView):
    def post(self, request):
        product_id = request.data.get('product_id')
        quantity = request.data.get('quantity', 1)
        try:
            cart, created = Cart.objects.get_or_create(author=request.user)
            product = Product.objects.get(id=product_id)
            cart_product, created = CartProduct.objects.get_or_create(cart=cart, product=product)
            if not created:
                cart_product.quantity += int(quantity)
            else:
                cart_product.quantity = int(quantity)
            cart_product.save()
            serializer = CartSerializer(cart)
            return Response({"status": "success", "cart": serializer.data}, status=status.HTTP_200_OK)
        except Product.DoesNotExist:
            return Response({"status": "error"}, status=status.HTTP_404_NOT_FOUND)

class RemoveProductFromCartView(APIView):
    def post(self, request):
        product_id = request.data.get('product_id')
        try:
            cart = Cart.objects.get(author=request.user)
            cart_product = CartProduct.objects.get(cart=cart, product_id=product_id)
            cart_product.delete()
            serializer = CartSerializer(cart)
            return Response({"status": "success", "cart": serializer.data}, status=status.HTTP_200_OK)
        except (Cart.DoesNotExist, CartProduct.DoesNotExist):
            return Response({"status": "error"}, status=status.HTTP_404_NOT_FOUND)

class LoginView(APIView):
    def post(self, request):
        username = request.data.get('username')
        password = request.data.get('password')
        user = authenticate(request, username=username, password=password)
        if user:
            login(request, user)
            serializer = UserSerializer(user)
            return Response({"status": "success", "user": serializer.data}, status=status.HTTP_200_OK)
        return Response({"status": "error"}, status=status.HTTP_400_BAD_REQUEST)

class LogoutView(APIView):
    def post(self, request):
        logout(request)
        return Response({"status": "success"}, status=status.HTTP_200_OK)

class RegisterView(APIView):
    def post(self, request):
        username = request.data.get('username')
        password = request.data.get('password')
        email = request.data.get('email')
        if User.objects.filter(username=username).exists():
            return Response({"status": "error"}, status=status.HTTP_400_BAD_REQUEST)
        user = User.objects.create_user(username=username, password=password, email=email)
        serializer = UserSerializer(user)
        return Response({"status": "success", "user": serializer.data}, status=status.HTTP_200_OK)
