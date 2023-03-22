from django.contrib import messages
from users.models import Favourites, Comments
from loguru import logger
from items_window.models import Item


class FavouritesHandler:

    """ Добавляет объявления в избранное и удаляет их от туда (Карточка объекта на главном экране и в ЛК)"""

    def __init__(self, request, item_id):
        self._request = request
        self._item_id = item_id

    def add_to_favs(self):
        """ Метод добавить в избранное """

        item = Item.objects.get(id=self._item_id)
        new_fav = Favourites(user=self._request.user,
                             item=item)
        new_fav.save()
        messages.info(self._request, 'Добавлено в избранное')

    def remove_from_favs(self):
        """ Метод удалить из избранного """

        return self._delete_fun()

    def _delete_fun(self):
        """ Функция удаления """

        cur_fav = Favourites.objects.filter(item__id__exact=self._item_id,
                                            user=self._request.user)
        cur_fav.delete()
        messages.info(self._request, 'Удалено из избранного')


