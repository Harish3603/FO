from django.contrib import admin

from .models import Product, CartItem
from .models import Customer,Dish,Payment
 
admin.site.register(Product)
admin.site.register(CartItem)
admin.site.register(Customer)
admin.site.register(Dish)
admin.site.register(Payment)