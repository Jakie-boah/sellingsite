# -*- coding: utf-8 -*-
from django.shortcuts import render, redirect
from items_window.models import *
from handlers.form import ReportForm
from loguru import logger
from users.models import Favourites, Comments
from users.form import CommentForm, FavouriteForm
from django.contrib import messages
from handlers.models import Report
from .filter import ListingFilter
from .item_utility import ItemFavouriteHandler, ItemReportHandler, ItemCommentHandler
from .card_urls import add_to_favs, remove_from_favs


def index(request):
    items = Item.objects.all()
    item_filter = ListingFilter(request.GET, queryset=items)

    params = {
        'item_filter': item_filter,
    }
    return render(request, './index.html', params)


def item(request, item_id):
    params = {}

    item = Item.objects.filter(id=item_id).first()
    images = Images.objects.filter(post__id__exact=item_id).all()

    params['item'] = item
    params['images'] = images

    if request.user.is_authenticated:
        comments = Comments.objects.filter(post__id__exact=item_id,
                                           user__id__exact=request.user.id).all()
        check_on_fav = Favourites.objects.filter(user=request.user,
                                                 item=item).first()
        check_on_rep = bool(Report.objects.filter(user=request.user,
                                                  item=item).first())

        params['comments'] = comments
        params['founded_fav'] = FavouriteForm(instance=check_on_fav)
        params['check_on_fav'] = check_on_fav
        params['check_on_rep'] = check_on_rep

    if request.method == 'POST':

        if request.POST['action'] == 'Добавить в избранное':
            form = FavouriteForm(request.POST)
            if form.is_valid():
                new_fav = ItemFavouriteHandler(form)
                new_fav.request = request
                new_fav.item = item
                new_fav.create_favourite()

                messages.success(request, 'Объявление успешно добавлено в избранное')
                return redirect('item', item_id)

        elif request.POST['action'] == 'Изменить':
            form = FavouriteForm(request.POST, instance=check_on_fav)
            if form.is_valid():
                fav = ItemFavouriteHandler(form)
                fav.edit_favourite()

                messages.success(request, 'Избранное успешно изменено')
                return redirect('item', item_id)

        elif request.POST['action'] == 'Пожаловаться':
            form = ReportForm(request.POST)
            if form.is_valid():
                report = ItemReportHandler(form, request, item)
                report.create_report()

                messages.success(request, 'Репорт отправлен')
                return redirect('item', item_id)

        elif request.POST['action'] == 'Прокомментировать':
            form = CommentForm(request.POST)
            if form.is_valid():
                comment = ItemCommentHandler(form, request, item)
                comment.create_comment()

                messages.success(request, 'Репорт отправлен')
                return redirect('item', item_id)

    else:

        params['favourite_form'] = FavouriteForm()
        params['report_form'] = ReportForm()
        params['comment_form'] = CommentForm()

    return render(request, './object.html', params)

