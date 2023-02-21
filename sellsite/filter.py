from django import forms
from items_window.models import Item
import django_filters


class ListingFilter(django_filters.FilterSet):

    price = django_filters.NumberFilter()

    min_price = django_filters.NumberFilter(field_name='price', lookup_expr='gte')
    max_price = django_filters.NumberFilter(field_name='price', lookup_expr='lte')

    total_surface = django_filters.NumberFilter()

    min_total_surface = django_filters.NumberFilter(field_name='total_surface', lookup_expr='gte')
    max_total_surface = django_filters.NumberFilter(field_name='total_surface', lookup_expr='lte')

    class Meta:
        model = Item
        fields = {'item_type': ['exact'],
                  'region': ['exact'],
                  }

    def __init__(self, *args, **kwargs):
        super(ListingFilter, self).__init__(*args, **kwargs)

        self.filters['item_type'].field.widget.attrs \
            .update({
            'class': 'btn',
            'style': 'height:57.6px; width: 180px; color-text: #000; background-color: #fff; border-right-color: #ced4da'

        })
        self.filters['region'].field.widget.attrs \
            .update({
            'class': 'btn',
            'style': 'height:57.6px; width: 180px; color-text: #000; background-color: #fff; border-right-color: #ced4da'

        })

        self.filters['min_price'].field.widget.attrs \
            .update({
            'min' : '0',
            'class': 'form-control stoim-ot',
            'placeholder': 'От'

        })
        self.filters['max_price'].field.widget.attrs \
            .update({
            'min': '0',
            'class': 'form-control stoim-do',
            'placeholder': 'До'

        })
        self.filters['min_total_surface'].field.widget.attrs \
            .update({
            'min': '0',
            'class': 'form-control area-ot',
            'placeholder': 'От',
            'step': "0.01"

        })
        self.filters['max_total_surface'].field.widget.attrs \
            .update({
            'min': '0',
            'class': 'form-control area-do',
            'placeholder': 'До',
            'step': "0.01"

        })


















