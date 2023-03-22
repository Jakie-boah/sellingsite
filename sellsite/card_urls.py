from django.http import HttpResponseRedirect
from .favorites_utility import FavouritesHandler


def add_to_favs(request, item_id):
    new_object = FavouritesHandler(request, item_id)
    new_object.add_to_favs()
    return HttpResponseRedirect(request.META.get('HTTP_REFERER') + f'#{item_id}')


def remove_from_favs(request, item_id):
    object = FavouritesHandler(request, item_id)
    object.remove_from_favs()
    return HttpResponseRedirect(request.META.get('HTTP_REFERER') + f'#{item_id}')


