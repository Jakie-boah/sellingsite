from django.shortcuts import render
from items_window.models import Item, Images
from loguru import logger


def index(request):
    items = Item.objects.all()
    images = Images.objects.all()
    params = {
        'items': items,
        'images': images
    }
    for i in items:
        logger.info(i.id)
        for j in images:
            logger.info(j.post)
            if int(i.id) == int(j.post.id):
                logger.info(j.image.url)

    return render(request, './index.html', params)


def item(request, item_id):
    item = Item.objects.filter(id=item_id).first()
    images = Images.objects.filter(post=item).all()
    # logger.info(item.description)
    for i in images:
        logger.info(i)
    params = {
        'item': item,
        'images': images
    }
    return render(request, './object.html', params)




