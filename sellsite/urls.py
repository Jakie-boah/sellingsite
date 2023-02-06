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


urlpatterns = [

    path('admin/', admin.site.urls),
    path('', index, name='index'),
    path('item<int:item_id>', item, name='item'),
    path('register', auth_url.register, name='register'),
    path('login', auth_url.log_in, name='login'),
    path('logout', auth_url.log_out, name='logout'),
    path('account', auth_url.account, name='account'),
    path('test', it_url.test, name='tets'),
    path('make_one', it_url.make_one, name='make_one'),
    path('contacts', hand_url.contacts, name='contacts'),


] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT) + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
