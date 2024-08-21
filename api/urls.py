from django.urls import path
from .views import (
    BannerListCreateView, BannerDetailView, CategoryListCreateView, CategoryDetailView,
    ProductListCreateView, ProductDetailView, CartListCreateView, CartDetailView, CartProductListCreateView, 
    CartProductDetailView, OrderListCreateView, OrderDetailView, ProductEnterListCreateView, 
    ProductEnterDetailView, InfoListCreateView, InfoDetailView, WishListListCreateView, 
    WishListDetailView, AddProductToCartView, RemoveProductFromCartView, 
    LoginView, LogoutView, RegisterView
)

urlpatterns = [
    path('banners/', BannerListCreateView.as_view(), name='banner-list-create'),
    path('banners/<int:pk>/', BannerDetailView.as_view(), name='banner-detail'),
    path('categories/', CategoryListCreateView.as_view(), name='category-list-create'),
    path('categories/<int:pk>/', CategoryDetailView.as_view(), name='category-detail'),
    path('products/', ProductListCreateView.as_view(), name='product-list-create'),
    path('products/<int:pk>/', ProductDetailView.as_view(), name='product-detail'),
    path('carts/', CartListCreateView.as_view(), name='cart-list-create'),
    path('carts/<int:pk>/', CartDetailView.as_view(), name='cart-detail'),
    path('cart-products/', CartProductListCreateView.as_view(), name='cart-product-list-create'),
    path('cart-products/<int:pk>/', CartProductDetailView.as_view(), name='cart-product-detail'),
    path('orders/', OrderListCreateView.as_view(), name='order-list-create'),
    path('orders/<int:pk>/', OrderDetailView.as_view(), name='order-detail'),
    path('product-enters/', ProductEnterListCreateView.as_view(), name='product-enter-list-create'),
    path('product-enters/<int:pk>/', ProductEnterDetailView.as_view(), name='product-enter-detail'),
    path('infos/', InfoListCreateView.as_view(), name='info-list-create'),
    path('infos/<int:pk>/', InfoDetailView.as_view(), name='info-detail'),
    path('wishlists/', WishListListCreateView.as_view(), name='wishlist-list-create'),
    path('wishlists/<int:pk>/', WishListDetailView.as_view(), name='wishlist-detail'),
    path('add-product-to-cart/', AddProductToCartView.as_view(), name='add-product-to-cart'),
    path('remove-product-from-cart/', RemoveProductFromCartView.as_view(), name='remove-product-from-cart'),
    path('login/', LoginView.as_view(), name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('register/', RegisterView.as_view(), name='register'),
]
