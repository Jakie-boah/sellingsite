from django.shortcuts import render, redirect
from django.utils.crypto import get_random_string
from .form import *
from loguru import logger
from django.contrib import messages
from django.contrib.auth import login
from .models import UserProfile, Favourites
from django.contrib.auth.decorators import login_required
# Create your views here.


@login_required(login_url='login')
def account(request):
    favourites = Favourites.objects.filter(user=request.user).all()

    params = {
        'favourites': favourites,
    }

    return render(request, './cabinet2.html', params)


