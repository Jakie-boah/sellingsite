from django.shortcuts import render, redirect
from ..form import *
from django.utils.crypto import get_random_string
from loguru import logger
from django.contrib import messages
from django.contrib.auth import login


def register(request):

    if request.method == 'POST':

        if request.POST['action'] == 'Зарегистрироваться':
            form = UserForm(request.POST)
            if form.is_valid():

                user = form.save()
                password = get_random_string(length=7)
                user.password = password
                user.save(update_fields=['password'])
                login(request, user)
                logger.info('Зареган новый пользователь')
                messages.success(request, 'Зарегистрирован новый пользователь')
                return redirect('index')
            else:
                logger.error('Ошибка')

    else:
        form = UserForm()

    params = {
        'form': form,
    }

    return render(request, './auth/register.html', params)