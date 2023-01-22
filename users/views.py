from django.shortcuts import render, redirect
from django.utils.crypto import get_random_string
from .form import *
from loguru import logger
from django.contrib import messages
from django.contrib.auth import login
from .models import UserProfile
# Create your views here.


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
                messages.success(request, 'Зареган новый пользователь')
            else:
                logger.error('Ошибка')

    else:
        form = UserForm()

    params = {
        'form': form,
    }

    return render(request, './register.html', params)


def log_in(request):
    if request.method == 'POST':

        if request.POST['action'] == 'Войти':
            form = LoginForm(request.POST)

            if form.is_valid():
                user = UserProfile.objects.filter(phone_number=form.cleaned_data['login']).first()
                if user is not None and user.password == form.cleaned_data['password']:
                    login(request, user)
                    logger.success('нашел. зашел')
                    messages.success(request, 'нашел. зашел')

                elif user.password != form.cleaned_data['password']:
                    messages.error(request, 'Ошибка в пароле')
                else:
                    messages.error(request, 'Пользователь с таким логином нет')
    else:
        form = LoginForm()

    params = {
        'form': form
    }

    return render(request, './login.html', params)


