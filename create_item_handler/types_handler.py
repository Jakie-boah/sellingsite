from loguru import logger


class Flat:
    """ Класс для создания объявления с типом Квартира """

    def __init__(self, post_form, postForm):
        self.post_form = post_form
        self.postForm = postForm.cleaned_data
        logger.info('Создаю новое объявление для объекта - Квартира')

    def create(self):
        self.post_form.price = int(self.postForm[f'{self.post_form.type}_price'].replace(' ', ''))
        self.post_form.floor = self.postForm['flat_floor']
        self.post_form.total_floors = self.postForm['flat_total_floor']
        self.post_form.material = self.postForm['flat_material']
        self.post_form.livin_surface = self.postForm['flat_livin_surface']
        logger.info('Создал новое объявление для объекта - Квартира')


class House:
    """ Класс для создания объявления с типом Дом """

    def __init__(self, post_form, postForm):
        self.post_form = post_form
        self.postForm = postForm.cleaned_data
        logger.info('Создаю новое объявление для объекта - Дом')

    def create(self):
        """ Метод создания """

        self.post_form.price = int(self.postForm[f'{self.post_form.type}_price'].replace(' ', ''))
        self.post_form.total_floors = self.postForm['house_total_floor']
        self.post_form.material = self.postForm['house_material']
        self.post_form.livin_surface = self.postForm['house_livin_surface']
        logger.info('Создал новое объявление для объекта - Дом')


class Garage:
    """ Класс для создания объявления с типом Гараж """

    def __init__(self, post_form, postForm):
        self.post_form = post_form
        self.postForm = postForm.cleaned_data
        logger.info('Создаю новое объявление для объекта - Гараж')

    def create(self):
        """ Метод создания """

        self.post_form.price = int(self.postForm[f'{self.post_form.type}_price'].replace(' ', ''))
        self.post_form.material = self.postForm['garage_material']
        logger.info('Создал новое объявление для объекта - Гараж')


class Com:
    """ Класс для создания объявления с типом Коммерческая недвижимость """

    def __init__(self, post_form, postForm):
        self.post_form = post_form
        self.postForm = postForm.cleaned_data
        logger.info('Создаю новое объявление для объекта - Коммерческая недвижимость')

    def create(self):
        """ Метод создания """

        self.post_form.price = int(self.postForm[f'{self.post_form.type}_price'].replace(' ', ''))
        self.post_form.floor = self.postForm['com_floor']
        self.post_form.total_floors = self.postForm['com_total_floor']
        self.post_form.material = self.postForm['com_material']
        logger.info('Создал новое объявление для объекта - Коммерческая недвижимость')


class Land:
    """ Класс для создания объявления с типом Участок """

    def __init__(self, post_form, postForm):
        self.post_form = post_form
        self.postForm = postForm.cleaned_data
        logger.info('Создаю новое объявление для объекта - Участок')

    def create(self):
        """ Метод создания """

        self.post_form.price = int(self.postForm[f'{self.post_form.type}_price'].replace(' ', ''))
        logger.info('Создал новое объявление для объекта - Участок')

