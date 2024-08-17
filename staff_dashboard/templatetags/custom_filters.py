from django import template

register = template.Library()


@register.filter(name='mul')
def mul(value, arg):
    """
    Multiply the given value by the argument.

    Args:
        value (float or int): The number to be multiplied.
        arg (float or int): The multiplier.

    Returns:
        float: The result of the multiplication.
    """
    return float(value) * arg
