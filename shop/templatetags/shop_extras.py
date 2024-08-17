from django import template

register = template.Library()


@register.filter(name='mul')
def mul(value, arg):
    """
    Multiplies the given value by a given argument.

    Args:
        value (float or str): The first value to be multiplied.
            Typically a numeric value or string representing a number.
        arg (float or str): The second value to multiply with. Also expected
            to be a numeric value or string representing a number.

    Returns:
        float: The result of of the multiplication.
    """
    return float(value) * float(arg)
