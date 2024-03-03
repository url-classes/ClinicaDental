from django import template

register = template.Library()

@register.filter
def multiply(value, arg):
    """Multiplies the given value by the arg."""
    return value * arg
