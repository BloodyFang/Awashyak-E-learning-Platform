
# Custome template filter.
from django import template

register = template.Library()

# Gets the model name for an object
@register.filter
def model_name(obj):

    try:
        return obj._meta.model_name

    except AttributeError:
        return None