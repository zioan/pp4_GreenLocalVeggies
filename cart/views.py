from django.shortcuts import render, redirect, get_object_or_404
from django.views.decorators.http import require_POST
from shop.models import Product
from decimal import Decimal
from .cart import Cart


@require_POST
def add_to_cart(request, product_id):
    cart = Cart(request)
    product = get_object_or_404(Product, id=product_id)
    quantity = Decimal(request.POST.get("quantity", "1"))
    cart.add(product=product, quantity=quantity, update_quantity=True)
    return redirect("cart_detail")


@require_POST
def remove_from_cart(request, product_id):
    cart = Cart(request)
    product = get_object_or_404(Product, id=product_id)
    cart.remove(product)
    return redirect("cart_detail")


def cart_detail(request):
    cart = Cart(request)
    cart_items = cart.get_items()
    print("Cart items:", cart_items)
    return render(request, "cart/index.html", {
        "cart": cart,
        "cart_items": cart_items
    })
