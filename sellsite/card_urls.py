from django.shortcuts import render, redirect
from users.models import Favourites, Comments
from django.contrib import messages
from items_window.models import Item
from loguru import logger
from django.http import HttpResponseRedirect


def add_to_favs(request, item_id):
    item = Item.objects.get(id=item_id)
    new_fav = Favourites(user=request.user,
                         item=item)
    new_fav.save()
    logger.info('Add')
    messages.info(request, 'Добавлено в избранное')
    return HttpResponseRedirect('/')


def delete_fun(request, item_id):
    cur_fav = Favourites.objects.filter(item__id__exact=item_id,
                                        user=request.user)
    cur_fav.delete()
    logger.info('Deleted')
    messages.info(request, 'Удалено из избранного')


def remove_from_favs(request, item_id):
    delete_fun(request, item_id)
    return HttpResponseRedirect('/')


def remove_from_favs_pp(request, item_id):
    delete_fun(request, item_id)
    return redirect('account')
