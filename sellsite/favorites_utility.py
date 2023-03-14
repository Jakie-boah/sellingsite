from django.contrib import messages
from users.models import Favourites, Comments
from loguru import logger
from items_window.models import Item


class FavouritesHandler:

    """ Добавляете объявления в избранное и удаляет их от туда (Карточка объекта на главном экране и в ЛК)"""

    def __init__(self, request, item_id):
        self.request = request
        self.item_id = item_id

    def add_to_favs(self):
        item = Item.objects.get(id=self.item_id)
        new_fav = Favourites(user=self.request.user,
                             item=item)
        new_fav.save()
        logger.info('Add')
        messages.info(self.request, 'Добавлено в избранное')

    def delete_fun(self):
        cur_fav = Favourites.objects.filter(item__id__exact=self.item_id,
                                            user=self.request.user)
        cur_fav.delete()
        logger.info('Deleted')
        messages.info(self.request, 'Удалено из избранного')

    def remove_from_favs(self):
        return self.delete_fun()
