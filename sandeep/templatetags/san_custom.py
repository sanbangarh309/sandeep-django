from django import template
register = template.Library()

def cut(value, arg):
    """Removes all values of arg from the given string"""
    return str (value).replace(arg, '')

register.filter('cut', cut)
