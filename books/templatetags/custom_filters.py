from django import template

register = template.Library()


@register.filter
def short_text(value, length=100):
    if not value:
        return ""

    value = str(value)
    length = int(length)

    if len(value) <= length:
        return value

    return value[:length] + "..."