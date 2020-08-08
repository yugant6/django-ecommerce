from django.contrib import admin

# Register your models here.
from .models import Item, Order, OrderItem, Address

admin.site.register(Item)
admin.site.register(Order)
admin.site.register(OrderItem)
admin.site.register(Address)
