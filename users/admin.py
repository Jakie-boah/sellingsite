from django.contrib import admin
from .models import UserProfile, Favourites
# Register your models here.
admin.site.register(UserProfile)
admin.site.register(Favourites)