from django.shortcuts import render
from .models import Favourites, Comments
from django.contrib.auth.decorators import login_required
from items_window.models import *
from loguru import logger
# Create your views here.


@login_required(login_url='login')
def account(request):

    items = Favourites.objects.filter(user=request.user).all()
    logger.info(items)
    for i in items:
        logger.info(i.item.name)
    comments = Comments.objects.filter(user__id__exact=request.user.id).all()
    images = Images.objects.all()
    params = {
        'items': items,
        'comments': comments,
        'images': images,
    }

    return render(request, './cabinet/cabinet.html', params)


