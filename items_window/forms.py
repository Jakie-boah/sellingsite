from django import forms
from .models import Item, Images
from phonenumber_field.formfields import PhoneNumberField
from items_window.handler import type_choices, item_type_choices
from geodata.models import Region


class ItemForm(forms.ModelForm):
    type = forms.CharField(max_length=50, label='Тип',
                           widget=forms.Select(choices=type_choices))

    item_type = forms.CharField(max_length=50, label='Тип объекта',
                                widget=forms.Select(attrs={
                                'id': 'sampleSelect'
                                }, choices=item_type_choices))
    com_floor = forms.IntegerField(required=False, label='Этаж',
                               widget=forms.NumberInput(attrs={
                                   'placeholder': 'Этаж',
                                   'data-select': '#sampleSelect',
                                   'data-option': 'com',
                                   'attribute': 'hidden'
                               }))
    flat_floor = forms.IntegerField(required=False, label='Этаж',
                               widget=forms.NumberInput(attrs={
                                   'placeholder': 'Этаж',
                                   'data-select': '#sampleSelect',
                                   'data-option': 'flat',
                                   'attribute': 'hidden'
                               }))

    house_total_floor = forms.IntegerField(required=False, label='Этажей всего',
                                     widget=forms.NumberInput(attrs={
                                         'placeholder': 'Этажей всего',
                                         'data-select': '#sampleSelect',
                                         'data-option': 'house',
                                         'attribute': 'hidden'
                                     }))
    com_total_floor = forms.IntegerField(required=False, label='Этажей всего',
                                     widget=forms.NumberInput(attrs={
                                         'placeholder': 'Этажей всего',
                                         'data-select': '#sampleSelect',
                                         'data-option': 'com',
                                         'attribute': 'hidden'
                                     }))
    flat_material = forms.CharField(required=False, max_length=50, label='Материал стен',
                               widget=forms.Select(attrs={
                                   'placeholder': 'Материал стен',
                                   'data-select': '#sampleSelect',
                                   'data-option': 'flat',
                                   'attribute': 'hidden'
                               }))
    house_material = forms.CharField(required=False, max_length=50, label='Материал стен',
                               widget=forms.Select(attrs={
                                   'placeholder': 'Материал стен',
                                   'data-select': '#sampleSelect',
                                   'data-option': 'house',
                                   'attribute': 'hidden'
                               }))
    garage_material = forms.CharField(required=False, max_length=50, label='Материал стен',
                               widget=forms.Select(attrs={
                                   'placeholder': 'Материал стен',
                                   'data-select': '#sampleSelect',
                                   'data-option': 'garage',
                                   'attribute': 'hidden'
                               }))
    com_material = forms.CharField(required=False, max_length=50, label='Материал стен',
                               widget=forms.Select(attrs={
                                   'placeholder': 'Материал стен',
                                   'data-select': '#sampleSelect',
                                   'data-option': 'com',
                                   'attribute': 'hidden'
                               }))
    total_surface = forms.IntegerField(required=False, widget=forms.NumberInput(attrs={'placeholder': 'Общая площадь'}),
                                       label='Общая площадь')
    flat_livin_surface = forms.IntegerField(required=False, label='Жилая площадь',
                                       widget=forms.NumberInput(attrs={
                                           'placeholder': 'Жилая площадь',
                                           'data-select': '#sampleSelect',
                                           'data-option': 'flat',
                                           'attribute': 'hidden'
                                       }))
    house_livin_surface = forms.IntegerField(required=False, label='Жилая площадь',
                                       widget=forms.NumberInput(attrs={
                                           'placeholder': 'Жилая площадь',
                                           'data-select': '#sampleSelect',
                                           'data-option': 'house',
                                           'attribute': 'hidden'
                                       }))
    price = forms.IntegerField(label='Цена')

    trade = forms.BooleanField(label='Возможность обмена',
                               widget=forms.CheckboxInput)
    description = forms.CharField(label='Описание', widget=forms.Textarea)

    class Meta:
        model = Item
        fields = ['phone_number', 'region', 'city', 'street']


class ImageForm(forms.ModelForm):
    image = forms.ImageField(label='Image')
    class Meta:
        model = Images
        fields = ('image', )
