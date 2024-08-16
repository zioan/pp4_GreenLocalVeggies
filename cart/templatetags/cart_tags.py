from django import template
from cart.cart import Cart

register = template.Library()


@register.simple_tag(takes_context=True)
def cart_item_count(context):
    """
    Returns the number of unique items in the cart.

    Args:
        context (dict): The template context.

    Returns:
        int: The number of unique items in the cart.
    """
    request = context['request']
    cart = Cart(request)
    return len(cart)


@register.simple_tag(takes_context=True)
def is_in_cart(context, product_id):
    """
    Checks if a product is in the cart.

    Args:
        context (dict): The template context.
        product_id: The ID of the product to check.

    Returns:
        bool: True if the product is in the cart, False otherwise.
    """
    request = context['request']
    cart = Cart(request)
    return str(product_id) in cart.cart


@register.simple_tag(takes_context=True)
def get_is_in_cart(context, product_id):
    """
    Alias for is_in_cart function.

    Args:
        context (dict): The template context.
        product_id: The ID of the product to check.

    Returns:
        bool: True if the product is in the cart, False otherwise.
    """
    request = context['request']
    cart = Cart(request)
    return str(product_id) in cart.cart


@register.simple_tag(takes_context=True)
def get_cart_quantity(context, product_id):
    """
    Gets the quantity of a specific product in the cart.

    Args:
        context (dict): The template context.
        product_id: The ID of the product to check.

    Returns:
        int: The quantity of the product in the cart, or 0 if not in cart.
    """
    request = context['request']
    cart = Cart(request)
    product_id_str = str(product_id)
    if product_id_str in cart.cart:
        return cart.cart[product_id_str]['quantity']
    return 0


@register.simple_tag(takes_context=True)
def cart_total_quantity(context):
    """
    Gets the total quantity of all items in the cart.

    Args:
        context (dict): The template context.

    Returns:
        int: The total quantity of all items in the cart.
    """
    request = context['request']
    cart = Cart(request)
    return cart.total_quantity()
