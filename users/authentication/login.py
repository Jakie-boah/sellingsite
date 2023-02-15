from django.shortcuts import render, redirect
from ..form import *
from django.contrib import messages
from django.contrib.auth import login


def log_in(request):
    if request.method == 'POST':

        if request.POST['action'] == 'Войти':
            form = LoginForm(request.POST)

            if form.is_valid():
                user = UserProfile.objects.filter(phone_number=form.cleaned_data['login']).first()
                if user is not None and user.password == form.cleaned_data['password']:
                    login(request, user)
                    return redirect('index')

                elif user.password != form.cleaned_data['password']:

                    messages.error(request, 'Ошибка в пароле')
                else:
                    messages.error(request, 'Пользователь с таким логином нет')
    else:
        form = LoginForm()

    params = {
        'form': form
    }

    return render(request, './auth/login.html', params)
