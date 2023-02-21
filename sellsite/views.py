from django.shortcuts import render, redirect
from items_window.models import *
from handlers.form import ReportForm
from loguru import logger
from users.models import Favourites, Comments
from users.form import CommentForm
from django.contrib import messages
from handlers.models import Report
from .filter import ListingFilter


def index(request):
    items = Item.objects.all()
    images = Images.objects.all()
    item_filter = ListingFilter(request.GET, queryset=items)

    params = {
        'item_filter': item_filter,
        'images': images
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
        check_on_fav = bool(Favourites.objects.filter(user=request.user,
                                                      item=item).first())
        check_on_rep = bool(Report.objects.filter(user=request.user,
                                                  item=item).first())

        params['comments'] = comments
        params['check_on_fav'] = check_on_fav
        params['check_on_rep'] = check_on_rep

    if request.method == 'POST':

        if request.POST['action'] == 'Объявление в избранное':
            new_fav = Favourites(user=request.user,
                                 item=item)
            new_fav.save()
            messages.success(request, 'Объявление успешно добавлено в избранное')
            logger.success('Объявление успешно добавлено в избранное')
            return redirect('item', item_id)

        elif request.POST['action'] == 'Пожаловаться':
            form = ReportForm(request.POST)
            if form.is_valid():
                report = form.save(commit=False)
                report.user = request.user
                report.item = item
                report.save()
                messages.success(request, 'Репорт отправлен')
                return redirect('item', item_id)

        elif request.POST['action'] == 'Прокомментировать':
            form = CommentForm(request.POST)
            if form.is_valid():
                comment = form.save(commit=False)
                comment.post = item
                comment.user = request.user
                comment.save()
                messages.success(request, 'Репорт отправлен')
                logger.success('Ком отправлен')
                return redirect('item', item_id)
    else:
        report_form = ReportForm()
        comment_form = CommentForm()
        params['report_form'] = report_form
        params['comment_form'] = comment_form

    return render(request, './object.html', params)


