from rest_framework import generics, status
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework.authtoken.models import Token
from django.contrib.auth import authenticate, login, logout
from main.models import Product, Category, Cart, CartProduct
from .serializers import ProductSerializer, CategorySerializer, UserSerializer, CartSerializer

class ProductList(generics.ListCreateAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

class ProductDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

class CategoryList(generics.ListCreateAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer

class CategoryDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer

class AddProductToCartView(APIView):
    def post(self, request):
        product_id = request.data.get('product_id')
        quantity = request.data.get('quantity', 1)
        try:
            cart, created = Cart.objects.get_or_create(user=request.user)
            product = Product.objects.get(id=product_id)
            cart_product, created = CartProduct.objects.get_or_create(cart=cart, product=product)
            if not created:
                cart_product.quantity += int(quantity)
                cart_product.save()
            else:
                cart_product.quantity = int(quantity)
                cart_product.save()
            serializer = CartSerializer(cart)
            return Response({
                "status": "success",
                "cart": serializer.data
            }, status=status.HTTP_200_OK)
        except Product.DoesNotExist:
            return Response({
                "status": "error",
                "message": "Product not found"
            }, status=status.HTTP_404_NOT_FOUND)

class RemoveProductFromCartView(APIView):
    def post(self, request):
        product_id = request.data.get('product_id')
        try:
            cart = Cart.objects.get(user=request.user)
            product = Product.objects.get(id=product_id)
            cart_product = CartProduct.objects.get(cart=cart, product=product)
            cart_product.delete()
            serializer = CartSerializer(cart)
            return Response({
                "status": "success",
                "cart": serializer.data
            }, status=status.HTTP_200_OK)
        except (Cart.DoesNotExist, Product.DoesNotExist, CartProduct.DoesNotExist):
            return Response({
                "status": "error",
                "message": "Product or cart not found"
            }, status=status.HTTP_404_NOT_FOUND)

@api_view(['POST'])
def register(request):
    serializer = UserSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=200)
    return Response(serializer.errors, status=400)

@api_view(['POST'])
def login_view(request):
    username = request.data.get('username')
    password = request.data.get('password')
    user = authenticate(username=username, password=password)
    if user:
        token, _ = Token.objects.get_or_create(user=user)
        login(request, user)
        return Response({'token': token.key}, status=200)
    return Response({'error': 'Xatolik'}, status=400)

@api_view(['POST'])
def logout_view(request):
    logout(request)
    return Response({'status': 'success'}, status=status.HTTP_200_OK)
