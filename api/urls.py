from django.urls import path
from .views import ProductList, ProductDetail, CategoryList, CategoryDetail, AddProductToCartView, RemoveProductFromCartView, register, login_view, logout_view

urlpatterns = [
    path('products/', ProductList.as_view(), name='product_list'),
    path('products/<int:pk>/', ProductDetail.as_view(), name='product_detail'),
    path('categories/', CategoryList.as_view(), name='category_list'),
    path('categories/<int:pk>/', CategoryDetail.as_view(), name='category_detail'),
    path('addproduct/', AddProductToCartView.as_view(), name='add_product_to_cart'),
    path('removeproduct/', RemoveProductFromCartView.as_view(), name='remove_product_from_cart'),
    path('register/', register, name='register'),
    path('login/', login_view, name='login'),
    path('logout/', logout_view, name='logout'),
]

