from django.shortcuts import render
from django.http import Http404
from .models import Product

# Create your views here.


def index(request):
    raise Exception("Testing 500 error handling")

    query = request.GET.get('q')
    if query:
        products = Product.objects.filter(name__icontains=query)
    else:
        products = Product.objects.all()
    return render(request, "shop/index.html", {"products": products})


def product_details(request, product_slug):
    try:
        product = Product.objects.get(slug=product_slug)
        step_value = 0.5 if product.allow_half_units else 1
    except Product.DoesNotExist:
        raise Http404("Product does not exist")

    return render(request, "shop/product-details.html", {
        "product": product,
        "step_value": step_value
    })
