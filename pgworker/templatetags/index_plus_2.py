from django import template
register = template.Library()
@register.filter(name='index_plus_2')
def index_plus_2(indexable, k):
    k=k*3+2
    return indexable[k]