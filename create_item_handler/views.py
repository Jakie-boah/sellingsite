from loguru import logger


class Flat:

    def __init__(self, post_form, postForm):
        logger.info('Создаю новое объявление для объекта - Квартира')
        print('init Flat' + f'{post_form}' + f'{postForm}')

    def create(self):
        logger.info('Создал')


class Post:
    def __init__(self, t, post_form, postForm):
        self.item_type = t
        self.post_form = post_form
        self.postForm = postForm

    def get_item_type(self):
        return eval(self.item_type.title())

    def check_item_type(self):
        item_type = self.get_item_type()
        return item_type(self.post_form, self.postForm)


class House:
    def __init__(self, post_form, postForm):
        logger.info('Создаю новое объявление для объекта - Дом')

    def create(self):
        logger.info('Создал дом')


class Garage:
    def __init__(self, post_form, postForm):
        logger.info('Создаю новое объявление для объекта - Гараж')

    def create(self):
        logger.info('Создал гараж')


class Com:
    def __init__(self, post_form, postForm):
        logger.info('Создаю новое объявление для объекта - Коммерческая недвижимость')

    def create(self):
        logger.info('Создал Коммерческая недвижимость')


class Land:
    def __init__(self, post_form, postForm):
        logger.info('Создаю новое объявление для объекта - Участок')

    def create(self):
        logger.info('Создал Участок')


