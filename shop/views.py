from django.shortcuts import render
from django.db import DatabaseError
from django.http import Http404
from .models import Product

# Create your views here.


def index(request):
    try:
        products = Product.objects.all()
        return render(request, "shop/index.html", {"products": products})
    except DatabaseError:
        return render(request, "shop/500.html")


def product_details(request, product_slug):
    try:
        product = Product.objects.get(slug=product_slug)
    except Product.DoesNotExist:
        raise Http404("Product does not exist")

    return render(request, "shop/product-details.html", {"product": product})


def custom_404_view(request, exception):
    return render(request, 'shop/404.html', status=404)
