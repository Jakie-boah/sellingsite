from django.shortcuts import render, redirect
from items_window.models import Item, Images
from loguru import logger
from users.models import Favourites
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

    item = Item.objects.filter(id=item_id).first()
    images = Images.objects.filter(post__id__contains=item.id).all()
    try:
        check_on_fav = bool(Favourites.objects.filter(user=request.user,
                                                      item=item).first())
        check_on_rep = bool(Report.objects.filter(user=request.user,
                                                  item=item).first())
    except TypeError:
        check_on_fav = False
        check_on_rep = False

    if request.method == 'POST':

        if request.POST['action'] == 'Объявление в избранное':
            new_fav = Favourites(user=request.user,
                                 item=item)
            new_fav.save()
            messages.success(request, 'Объявление успешно добавлено в избранное')
            logger.success('Объявление успешно добавлено в избранное')
            return redirect('item', item_id)

        elif request.POST['action'] == 'Пожаловаться':
            new_rep = Report(user=request.user,
                             item=item,
                             report_text=request.POST['comment'])
            new_rep.save()
            messages.success(request, 'Репорт отправлен')
            logger.success('Репорт отправлен')
            return redirect('item', item_id)

    params = {
        'item': item,
        'images': images,
        'check_on_fav': check_on_fav,
        'check_on_rep': check_on_rep
    }
    return render(request, './object.html', params)




