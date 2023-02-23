from django import template
from ..views import Favourites
register = template.Library()
from loguru import logger


@register.filter(name='spaced_format')
def spaced_format(value):
    left = int(value / 10000)
    right = value % 10000
    return '{:03} {:04}'.format(left, right)


@register.filter(name='check')
def favs_filter(item_id, user):
    check_on_fav = bool(Favourites.objects.filter(user=user,
                                                  item__id__exact=item_id).first())
    return check_on_fav

