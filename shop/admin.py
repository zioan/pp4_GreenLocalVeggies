from django.contrib import admin
from .models import Product


class ProductAdmin(admin.ModelAdmin):
    """
    Customizes the admin interface for the Product model.

    This class configures how the Product model is displayed and interacted
    with in the Django admin panel.
    """
    list_display = ("name", "category", "price",
                    "stock", "unit")
    search_fields = ["name", "category", "price"]
    list_filter = ["category"]
    prepopulated_fields = {'slug': ('name',)}


admin.site.register(Product, ProductAdmin)
