from django import template
from cart.cart import Cart

register = template.Library()


@register.simple_tag(takes_context=True)
def cart_item_count(context):
    request = context['request']
    cart = Cart(request)
    return len(cart)


@register.simple_tag(takes_context=True)
def is_in_cart(context, product_id):
    request = context['request']
    cart = Cart(request)
    return str(product_id) in cart.cart


@register.simple_tag(takes_context=True)
def get_is_in_cart(context, product_id):
    request = context['request']
    cart = Cart(request)
    return str(product_id) in cart.cart


@register.simple_tag(takes_context=True)
# quantity per product
def get_cart_quantity(context, product_id):
    request = context['request']
    cart = Cart(request)
    product_id_str = str(product_id)
    if product_id_str in cart.cart:
        return cart.cart[product_id_str]['quantity']
    return 0


@register.simple_tag(takes_context=True)
# cart total quantity
def cart_total_quantity(context):
    request = context['request']
    cart = Cart(request)
    return cart.total_quantity()
