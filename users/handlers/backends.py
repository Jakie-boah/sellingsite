from django.contrib.auth import backends, get_user_model
from django.core.exceptions import ObjectDoesNotExist
from django.contrib import messages
from django.contrib.auth.hashers import check_password
from loguru import logger

UserModel = get_user_model()


class HashedPasswordAuthBackend(backends.ModelBackend):

    def authenticate(self, request, phone_number=None, password=None, **kwargs):
        if phone_number is None:
            user_login = kwargs.get(UserModel.USERNAME_FIELD)
        else:
            try:
                user = UserModel.objects.get(phone_number=phone_number)
                logger.info(user.password)
                if check_password(password, user.password):
                    return user

                else:
                    messages.error(request, 'Ошибка в пароле')
                    return False

            except ObjectDoesNotExist:
                messages.error(request, 'Пользователь с таким логином нет')
                return False

        return super().authenticate(request, phone_number, password, **kwargs)
