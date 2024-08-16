from django.shortcuts import render, redirect, get_object_or_404
from django.views.decorators.http import require_POST
from django.core.exceptions import ValidationError
from django.http import JsonResponse
from django.contrib import messages
from shop.models import Product
from decimal import Decimal
from .cart import Cart


@require_POST
def add_to_cart(request, product_id):
    """
    Add a product to the cart.

    Args:
        request: The HTTP request object.
        product_id (int): The ID of the product to add.

    Returns:
        JsonResponse: A JSON response indicating success or failure.
    """
    try:
        cart = Cart(request)
        product = get_object_or_404(Product, id=product_id)
        quantity = Decimal(request.POST.get('quantity', '1'))

        # Validate quantity
        if quantity <= 0 or quantity > product.stock:
            raise ValidationError("Invalid quantity.")

        cart.add(product=product, quantity=quantity, update_quantity=False)

        return JsonResponse({
            'status': 'success',
            'message': f"{quantity} {product.unit} of {product.name} added to cart.",
            'cart_count': len(cart),
            'product_in_cart': True
        })

    except ValidationError as e:
        return JsonResponse({'status': 'error', 'message': str(e)}, status=400)
    except Exception as e:
        return JsonResponse({
            'status': 'error', 'message': str(e)}, status=500)


@require_POST
def update_cart(request, product_id):
    """
    Update the quantity of a product in the cart.

    Args:
        request: The HTTP request object.
        product_id (int): The ID of the product to update.

    Returns:
        JsonResponse: A JSON response with updated cart information.
    """
    cart = Cart(request)
    product = get_object_or_404(Product, id=product_id)
    quantity = int(request.POST.get('quantity'))

    if quantity > 0:
        cart.add(product=product, quantity=quantity, update_quantity=True)
    else:
        cart.remove(product)

    return JsonResponse({
        'status': 'success',
        'cart_total': cart.get_total_price(),
        'cart_count': cart.total_quantity(),
    })


@require_POST
def remove_from_cart(request, product_id):
    """
    Remove a product from the cart.

    Args:
        request: The HTTP request object.
        product_id (int): The ID of the product to remove.

    Returns:
        HttpResponseRedirect: Redirects to the cart detail page.
    """
    cart = Cart(request)
    product = get_object_or_404(Product, id=product_id)
    cart.remove(product)
    messages.success(request, f"{product.name} removed from cart.")
    return redirect("cart_detail")


def cart_detail(request):
    """
    Display the cart details.

    Args:
        request: The HTTP request object.

    Returns:
        HttpResponse: Renders the cart detail page.
    """
    cart = Cart(request)
    cart_items = cart.get_items()
    return render(request, "cart/index.html", {
        "cart": cart,
        "cart_items": cart_items
    })
