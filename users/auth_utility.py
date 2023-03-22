#!/usr/bin/env python
# -*- coding: utf-8 -*-
from loguru import logger
from django.utils.crypto import get_random_string
from django.contrib.auth.hashers import make_password
from django.contrib import messages
from django.shortcuts import redirect
from django.contrib.auth import get_user_model
from django.contrib.auth import login
from django.http import HttpResponseRedirect
from .handlers.backends import HashedPasswordAuthBackend
import smtplib


class RegisterHandler:
    """
    Объект отвечает за регистрацию пользователя, включая подтверждение почты.
    Принимает 3 возможных параметра:
        1) request - request django
        2) form - прошедшая валидацию форма django
        3) user_id - параметр, необходимый при вызове метода confirmation, -- подтверждение почты и активация юзера.
                    Изначально равен None, чтобы при регистрации не возникало ошибки
    """
    gmail_user = 'mrkidrock228@gmail.com'
    gmail_app_password = 'qwyykoohcxmnruer'

    def __init__(self, request, form, user_id=None):
        self.request = request
        self.form = form

        if user_id is not None:
            self.user = user_id

    @property
    def user(self):
        return self._user

    @user.setter
    def user(self, value):
        """
        Поиск уже зарегистрированного пользователя (но пока еще не активного) в Модели юзеров.
        Метод используется исключительно при подтверждении почты и активации юзера
        """

        self._user = RegisterHandler.user_model(value)

    def register(self):
        """
         Метод регистрации пользователя с дальнейшим перенаправлением на подтверждение и активацию аккаунта
        """

        user = self.form.save()
        password = get_random_string(length=7)
        logger.info(password)
        user.password = password
        user.save(update_fields=['password'])
        self._send_email(user)
        messages.success(self.request, 'Чтобы закончить регистрацию введите пароль.\n'
                                       'Он отправлен на почту')
        return redirect('register_confirm', user.id)

    def confirmation(self):
        """
        Метод подтверждения и автоматической активации пользователя
        """

        if self.user:
            if self.form.cleaned_data['password'] == self.user.password:
                self.user.password = make_password(self.user.password)
                logger.info(self.user.password)
                self.user.is_active = True
                self.user.save()
                login(self.request, self.user, backend='django.contrib.auth.backends.ModelBackend')
                messages.success(self.request, 'Зарегистрирован новый пользователь')
                return redirect('index')

            else:
                messages.error(self.request, 'Неверный пароль')
                return HttpResponseRedirect(self.request.META.get('HTTP_REFERER'))
        else:
            raise ValueError('Параметр user_id равен None')

    @staticmethod
    def _send_email(user):
        """
        Отправка сообщения на почту пользователя, содержащее пароль от аккаунта
        """

        sent_from = RegisterHandler.gmail_user
        sent_to = ['vanogalen@yandex.ru', 'vanogalen@yandex.ru']
        sent_subject = "password"
        sent_body = (user.password)

        email_text = """\
            From: %s
            To: %s
            Subject: %s

            %s
            """ % (sent_from, ", ".join(sent_to), sent_subject, sent_body)

        server = smtplib.SMTP_SSL('smtp.gmail.com', 465)
        server.ehlo()
        server.login(RegisterHandler.gmail_user, RegisterHandler.gmail_app_password)
        server.sendmail(sent_from, sent_to, email_text)
        server.close()

    @staticmethod
    def user_model(user_id):
        Users = get_user_model()
        return Users.objects.get(id=user_id)


class LoginHandler:
    """
    Объект отвечает за авторизацию пользователя.
    Принимает 2 параметра:
        1) request - request django
        2) form - прошедшая валидацию форма django
    """

    def __init__(self, request, form):
        self.request = request
        self.form = form.cleaned_data

    def _authenticate_user(self):
        """
        Метод поиск юзера в бд при логинировании (аутентификация) с поднятием все возможных валидаций
        На выхлопе либо поднимает ошибку, либо выдает юзера
        """

        user = HashedPasswordAuthBackend().authenticate(
            request=self.request,
            phone_number=self.form['login'],
            password=self.form['password']
        )
        return user

    def log_in(self):
        """
        Метод авторизации после нахождения юзера и проверки пароля и логина
        """

        user = self._authenticate_user()
        if user:
            login(self.request, user, backend='django.contrib.auth.backends.ModelBackend')
            return redirect('index')
