from django.urls import path
from .views import ProductList, ProductDetail, CategoryList, CategoryDetail, register, login_view

urlpatterns = [
    path('products/list/', ProductList.as_view(), name='product_list'),
    path('products/detail/<int:pk>/', ProductDetail.as_view(), name='product_detail'),

    path('category/list/', CategoryList.as_view(), name='category_list'),
    path('category/detail/<int:pk>/', CategoryDetail.as_view(), name='category_detail'),
    
    path('register/', register, name='register'),
    path('login/', login_view, name='login'),
]
