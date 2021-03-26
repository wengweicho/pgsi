from django import template
register = template.Library()
@register.filter(name='index')
def index(indexable, i):
    i=i*3
    return indexable[i]