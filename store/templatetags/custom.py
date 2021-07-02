from django import template

register = template.Library()


@register.filter(name='multiply')
def multiply(n,m):
    return n*m
