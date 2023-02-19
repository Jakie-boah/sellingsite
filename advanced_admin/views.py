from django.shortcuts import render
from django.contrib.auth.decorators import permission_required
from .models import AdminsRegions, UserProfile
from loguru import logger
from items_window.models import Item
# Create your views here.


@permission_required('items_window.control_new_items', login_url='login')
def extended_page(request):

    region = AdminsRegions.objects.get(admin=request.user).region
    items = Item.objects.filter(public=False, region=region)

    return render(request, './advanced_admin/extended_page.html', {'items': items})



