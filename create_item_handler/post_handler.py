from .types_handler import *
from items_window.models import Images


class Post:
    """ Начальный хендлер создания объявления. Он проверяет тип и перенаправляет на класс создания """

    def __init__(self, item_type, post_form, postForm):
        self.item_type = item_type
        self.post_form = post_form
        self.postForm = postForm

    def get_item_type(self):
        """ Форматирование строки в тип класса """

        return eval(self.item_type.title())

    def get_item_class(self):
        """ Получение класса, основываясь на типе объявления """

        item_type = self.get_item_type()
        return item_type(self.post_form, self.postForm)


class PostMainImage:
    """ Объект по установке в объявлении основного изображения """

    def __init__(self, main_imageForm, post_form):
        self.main_imageForm = main_imageForm
        self.post_form = post_form
        logger.info('Инициализирую установку основного изображения')

    def set_main_image(self):
        """ Метод установки основного изображения """

        if self.main_imageForm.cleaned_data['image']:
            main_imageForm = self.main_imageForm.save(commit=False)
            main_imageForm.post = self.post_form
            main_imageForm.active = True
            self.post_form.save()
            main_imageForm.save()
            logger.info('Основное изображение установлено')

        else:
            self.post_form.no_pictures = True
            self.post_form.save()
            logger.info('Основное изображение при создании объявления отсутствовало. Поле осталось пустым')


class PostImages:
    """ Объект по установке всех изображений """

    def __init__(self, formset, post_form):
        self.formset = formset
        self.post_form = post_form
        logger.info('Инициализирую установку всех изображений')

    def set_rest_images(self):
        """ Метод установки всех изображений """

        for form in self.formset:
            if form:
                image = form['image']
                photo = Images(post=self.post_form, image=image)
                photo.save()
                logger.info('Изображения успешно подвязаны к объявлению')
            else:
                logger.info('Изображения отсутствуют. Нечего сохранять')

