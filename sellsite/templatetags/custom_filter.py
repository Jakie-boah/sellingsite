from django import template
from ..views import Favourites, Images, Comments
register = template.Library()
from loguru import logger


@register.filter(name='spaced_format')
def spaced_format(value):
    left = int(value / 10000)
    right = value % 10000
    return '{:03} {:04}'.format(left, right)


@register.filter(name='check')
def fav_filter(item_id, user):
    check_on_fav = bool(Favourites.objects.filter(user=user,
                                                  item__id__exact=item_id).first())
    return check_on_fav


@register.filter(name='imagefilter')
def imagefilter(post_id):
    images = Images.objects.filter(post__id__exact=post_id).all()
    return images


@register.filter(name='commentsfilter')
def commentsfilter(user_id, item_id):
    comments = Comments.objects.filter(user__id__exact=user_id,
                                       post__id__exact=item_id).all()
    return comments


@register.filter(name='isfavs')
def fav_control(user):
    check = bool(Favourites.objects.filter(user=user).first())
    return check
