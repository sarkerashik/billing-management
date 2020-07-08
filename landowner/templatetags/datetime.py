from datetime import datetime
from django import template


register = template.Library()


@register.filter
def datetimeformat(value,format='%Y-%m-%d %H:%M:%S'):
    return datetime.fromtimestamp(value).strftime(format)

@register.filter
def dateformat(value,format='%Y-%m-%d'):
    return datetime.fromtimestamp(value).strftime(format)




        
