from django.shortcuts import render, redirect
from django.contrib.auth.decorators import permission_required
from ..models import AdminsRegions, UserProfile
from loguru import logger
from handlers.models import BlackList
from django.contrib import messages
from items_window.models import Item, Images
from django.core.exceptions import ObjectDoesNotExist
from geodata.models import Region
# Create your views here.


@permission_required('items_window.control_new_items', login_url='login')
def extended_page_regions(request):

    params = {}
    try:
        regions = AdminsRegions.objects.get(admin=request.user).region.all()
        params['regions'] = regions

    except ObjectDoesNotExist:
        messages.error(request, 'У пользователя есть доступ на страницу расширенного доступа,'
                                ' но необходимо выбрать регион/ы, в котором данный пользователь может работать')

    return render(request, './advanced_admin/extend_item/extended_item_regions.html', params)


@permission_required('items_window.control_new_items', login_url='login')
def extended_item_list(request, region_id):
    items = Item.objects.filter(public=False, region=Region.objects.get(id=region_id)).all()
    region = Region.objects.get(id=region_id).alternate_names
    return render(request, './advanced_admin/extend_item/extended_item_list.html', {'region': region,
                                                                        'items': items})


@permission_required('items_window.control_new_items', login_url='login')
def extended_item(request, item_id):

    item = Item.objects.filter(id=item_id).first()
    images = Images.objects.filter(post__id__exact=item_id).all()

    if request.method == 'POST':

        if request.POST['action'] == 'Вернуться к списку объявлений':
            return redirect('extended_item_list', item.region.id)

        elif request.POST['action'] == 'Опубликовать':
            item.public = True
            item.save()
            messages.info(request, 'Объявление одобрено и опубликовано')
            return redirect('extended_item_list', item.region.id)

        elif request.POST['action'] == 'Удалить объявление':
            region_id = item.region.id
            item.delete()
            messages.info(request, 'Объявление удалено')
            return redirect('extended_item_list', region_id)

        elif request.POST['action'] == 'Заблокировать пользователя':
            new_number = BlackList(phone_number=item.phone_number)
            new_number.save()
            messages.info(request, 'Пользователь заблокирован. Объявления скрыты')
            return redirect('extended_item_list', item.region.id)

    params = {
        'item': item,
        'images': images
    }

    return render(request, './advanced_admin/extend_item/extended_item.html', params)

