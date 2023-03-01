"""
sellsite URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.conf.urls.static import static
from django.conf import settings
from django.contrib import admin
from django.urls import path
from .views import *
from users import views as auth_url
from items_window import views as it_url
from handlers import views as hand_url
from advanced_admin import views as extend_rights
urlpatterns = [

    path('admin/', admin.site.urls),
    path('', index, name='index'),
    path('item<int:item_id>', item, name='item'),
    path('register', auth_url.register, name='register'),
    path('login', auth_url.log_in, name='login'),
    path('logout', auth_url.log_out, name='logout'),
    path('account', auth_url.account, name='account'),
    path('make_one', it_url.make_one, name='make_one'),
    path('contacts', hand_url.contacts, name='contacts'),
    path('add_to_favs<int:item_id>', add_to_favs, name='add_to_favs'),
    path('remove_from_favs<int:item_id>', remove_from_favs, name='remove_from_favs'),
    path('favs_for_print', auth_url.favs_for_print, name='favs_for_print'),
    path('test', it_url.test, name='test'),

    path('extend_access', extend_rights.extend_access, name='extended_page'),
    path('extended_page_regions', extend_rights.extended_page_regions, name='extended_page_regions'),
    path('extended_item_list<int:region_id>', extend_rights.extended_item_list, name='extended_item_list'),
    path('extended_item<int:item_id>', extend_rights.extended_item, name='extended_item'),

    path('extended_black_list', extend_rights.extended_black_list, name='extended_black_list'),
    path('extended_black_list_page<int:phone_id>', extend_rights.extended_black_list_page, name='extended_black_list_page'),
    path('extended_black_list_add', extend_rights.extended_black_list_add, name='extended_black_list_add'),

    path('extended_reports', extend_rights.extended_reports, name='extended_reports'),
    path('extended_report_page<int:report_id>', extend_rights.extended_report_page, name='extended_report_page'),

] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT) + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
