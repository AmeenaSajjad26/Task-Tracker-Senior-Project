from django import template
register = template.Library()

# Method 1 for django queryset (Better)
@register.filter    
def intersection(queryset1,arg):

    return queryset1 & queryset2