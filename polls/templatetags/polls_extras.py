from django import template

register = template.Library()

@register.filter
def dict_get(dictionary, key):
    """Get a value from a dictionary by key"""
    if dictionary and isinstance(dictionary, dict):
        return dictionary.get(key, 0)
    return 0
