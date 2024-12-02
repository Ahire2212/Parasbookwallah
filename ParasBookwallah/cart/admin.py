

# Register your models here.
from django.contrib import admin
from .models import Order,OrderItem

# Register your models here.


admin.site.register(Order)
class OrderItemAdmin(admin.ModelAdmin):
    list_display=["Order","products","quantity"]

admin.site.register(OrderItem,OrderItemAdmin)
