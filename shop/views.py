from django.shortcuts import render, get_object_or_404
from .models import Product

# Create your views here.


def index(request):
    products = Product.objects.all()
    return render(request, "shop/index.html", {"products": products})


def product_details(request, product_slug):
    product = get_object_or_404(Product, slug=product_slug)
    return render(request, "shop/product-details.html", {
        "product": product
    })
