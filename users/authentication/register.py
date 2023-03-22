from django.shortcuts import render, redirect
from ..form import *
from ..auth_utility import RegisterHandler


def register(request):

    if request.method == 'POST':

        if request.POST['action'] == 'Зарегистрироваться':
            form = UserForm(request.POST)

            if form.is_valid():
                new_user = RegisterHandler(request, form)
                return new_user.register()

    else:
        form = UserForm()

    params = {
        'form': form,
    }

    return render(request, './auth/register.html', params)


def register_confirm(request, user_id):
    if request.method == 'POST':

        if request.POST['action'] == 'Войти':
            form = RegisterConfirm(request.POST)

            if form.is_valid():
                new_user = RegisterHandler(request, form, user_id)
                return new_user.confirmation()

    else:
        form = RegisterConfirm()

    params = {
        'form': form,
    }

    return render(request, './auth/register_confirm.html', params)
