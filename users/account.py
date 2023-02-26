from django.shortcuts import render
from .models import Favourites, Comments
from django.contrib.auth.decorators import login_required
from items_window.models import *
from loguru import logger
# Create your views here.


@login_required(login_url='login')
def account(request):

    items = Favourites.objects.filter(user=request.user).all()
    comments = Comments.objects.filter(user__id__exact=request.user.id).all()
    images = Images.objects.all()
    params = {
        'items': items,
        'comments': comments,
        'images': images,
    }

    return render(request, './cabinet/cabinet.html', params)


@login_required(login_url='login')
def favs_for_print(request):
    items = Favourites.objects.filter(user=request.user).all()
    return render(request, './cabinet/handlers/favourites_for_pdf.html', {'items': items})
