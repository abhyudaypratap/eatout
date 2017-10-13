from django import template
from django.utils.safestring import mark_safe
import json
import re

register = template.Library()


@register.filter
def to_json(value):
    return mark_safe(json.dumps(value))


@register.filter
def remove_underscores(value):
    return value.replace("_", " ")


@register.filter
def account_name(value):
    account_type = {'0': 'Free', '1': 'Basic', '2': 'Pro'}
    return account_type[value]


@register.filter
def get_item(dictionary, key):
    return dictionary.get(key)


@register.filter
def get_text(value):
    return(re.sub('<[^>]*>', '', value))
