
from loguru import logger


class CodeHandler:
    """ Объект для наследования, чтобы оптимизировать код """

    def __init__(self, form, request, item):
        self.form = form
        self.request = request
        self.item = item

    @property
    def form(self):
        return self._form

    @property
    def request(self):
        return self._request

    @property
    def item(self):
        return self._item

    @form.setter
    def form(self, value):
        """ Установка формы """

        self._form = value

    @request.setter
    def request(self, value):
        """ Создание аттрибута request из которого код вытащит user """

        self._request = value

    @item.setter
    def item(self, value):
        """ Создание аттрибута item. Он регулирует объект, с которым будет работа """

        self._item = value


class ItemFavouriteHandler:

    """ Утилита на Добавление/Изменение объекта в избранном через объявление на прямую
     self.form - заведомо созданная форма джанго
     self._request - request, стандартный параметр рендеринга джанго
     self._item - объект, который будет добавлен в избранное """

    def __init__(self, form):
        self.form = form
        self._request = None
        self._item = None

    @property
    def form(self):
        return self._form

    @form.setter
    def form(self, value):
        """ Установка формы """

        self._form = value

    @property
    def request(self):
        return self._request

    @request.setter
    def request(self, value):
        """ Создание аттрибута request из которого код вытащит user """

        self._request = value

    @property
    def item(self):
        return self._item

    @item.setter
    def item(self, value):
        """ Создание аттрибута item. Он регулирует объект, который будет добавлен в избранное """

        self._item = value

    def create_favourite(self):
        """ Метод добавления в избранное """

        if self._request and self._item:
            new_fav = self.form.save(commit=False)
            new_fav.user = self.request.user
            new_fav.item = self.item
            new_fav.save()
            logger.success('Объявление успешно добавлено в избранное')
        else:
            raise AttributeError('Необходимо задать параметр request и item')

    def edit_favourite(self):
        """ Метод изменения избранного """

        self.form.save()
        logger.success('Избранное успешно изменено')


class ItemReportHandler(CodeHandler):
    """ Утилита на создание репорта через объявление на прямую """

    def __init__(self, form, request, item):
        super().__init__(form, request, item)

    def create_report(self):
        """ Метод создания репорта """

        report = self.form.save(commit=False)
        report.user = self.request.user
        report.item = self.item
        report.save()
        logger.success('Репорт успешно отправлен')


class ItemCommentHandler(CodeHandler):
    """ Утилита на создание комментарии к объявлению """

    def __init__(self, form, request, item):
        super().__init__(form, request, item)

    def create_comment(self):
        """ Метод создания нового комментария """

        comment = self.form.save(commit=False)
        comment.post = self.item
        comment.user = self.request.user
        comment.save()
        logger.success('Комментарий создан')

