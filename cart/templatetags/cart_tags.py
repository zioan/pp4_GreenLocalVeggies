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
