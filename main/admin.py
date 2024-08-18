from django.contrib import admin
from main.models import Category, Product, Cart, CartProduct

admin.site.register(Category)
admin.site.register(Product)
admin.site.register(CartProduct)
admin.site.register(Cart)