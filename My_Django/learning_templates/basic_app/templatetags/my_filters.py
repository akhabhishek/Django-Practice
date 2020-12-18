from django import template

register = template.Library()

@register.filter(name='cut_string')
def cut(value, arg):
    """
    This cuts out all the occurences of arg from the string - values
    """
    return value.replace(arg,'')
