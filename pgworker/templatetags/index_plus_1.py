from django import template
register = template.Library()
@register.filter(name='index_plus_1')
def index_plus_1(indexable, j):
    j=j*3+1
    return indexable[j]