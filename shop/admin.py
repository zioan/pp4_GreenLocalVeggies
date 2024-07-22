from django.contrib import admin
from .models import Product

# Register your models here.


class ProductAdmin(admin.ModelAdmin):
    list_display = ("name", "category", "price",
                    "stock", 'allow_half_units', "unit")
    search_fields = ["name", "category", "price"]
    list_filter = ["category"]
    prepopulated_fields = {'slug': ('name',)}


admin.site.register(Product, ProductAdmin)
