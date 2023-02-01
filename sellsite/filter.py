from django import forms
from items_window.models import Item
import django_filters


class ListingFilter(django_filters.FilterSet):

    class Meta:
        model = Item
        fields = {'item_type': ['exact']}


















