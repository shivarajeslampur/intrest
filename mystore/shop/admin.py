from django.contrib import admin
from .product import Product
from .category import Category
from .customer import Customer

class Categoryinfo(admin.ModelAdmin):
    list_display = ["name"]

class Productinfo(admin.ModelAdmin):
    list_display = ["name", "category", "price"]

class Customerinfo(admin.ModelAdmin):
    list_display = ["firstname", "lastname", "email"]

# Register your models here.
admin.site.register(Product, Productinfo)
admin.site.register(Category, Categoryinfo)
admin.site.register(Customer, Customerinfo)



