from django.shortcuts import render, redirect
from ..form import *
from ..auth_utility import LoginHandler


def log_in(request):
    if request.method == 'POST':

        if request.POST['action'] == 'Войти':
            form = LoginForm(data=request.POST)

            if form.is_valid():
                user = LoginHandler(request, form)
                return user.log_in()

    else:
        form = LoginForm()

    params = {
        'form': form
    }

    return render(request, './auth/login.html', params)
