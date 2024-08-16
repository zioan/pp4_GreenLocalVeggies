from django import template

register = template.Library()


@register.filter(name='mul')
def mul(value, arg):
    """
    Multiply a numeric value by a given argument.

    Args:
        value (float or int): The number to be multiplied.
        arg (float or int): The multiplier.

    Returns:
        float: The result of the multiplication.
    """
    return float(value) * arg
