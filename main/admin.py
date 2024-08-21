from django.contrib import admin
from .models import (
    Banner, Category, Product, ProductImg, Cart, CartProduct, 
    Order, ProductEnter, Info, WishList
)

admin.site.register(Banner)
admin.site.register(Category)
admin.site.register(Product)
admin.site.register(ProductImg)
admin.site.register(Cart)
admin.site.register(CartProduct)
admin.site.register(Order)
admin.site.register(ProductEnter)
admin.site.register(Info)
admin.site.register(WishList)
