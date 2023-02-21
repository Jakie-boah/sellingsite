from django import forms
from .models import Item, Images
from possible_choices.models import MaterialChoices
from django.core.exceptions import ValidationError


class ItemForm(forms.ModelForm):
    com_floor = forms.IntegerField(required=False, label='Этаж',
                                   widget=forms.NumberInput(attrs={
                                       'class': 'form-control',
                                       'placeholder': 'Этаж',
                                       'data-select': '#sampleSelect',
                                       'data-option': 'com',
                                       'attribute': 'hidden',
                                       'min': '0',
                                       'max': '99'
                                   }))
    flat_floor = forms.IntegerField(required=False, label='Этаж',
                                    widget=forms.NumberInput(attrs={
                                        'class': 'form-control',
                                        'placeholder': 'Этаж',
                                        'data-select': '#sampleSelect',
                                        'data-option': 'flat',
                                        'attribute': 'hidden',
                                        'min': '0',
                                        'max': '99'
                                    }))
    flat_total_floor = forms.IntegerField(required=False, label='Этажность дома',
                                          widget=forms.NumberInput(attrs={
                                              'class': 'form-control',
                                              'placeholder': 'Этажность дома',
                                              'data-select': '#sampleSelect',
                                              'data-option': 'flat',
                                              'attribute': 'hidden',
                                              'min': '0',
                                              'max': '99'
                                          }))
    house_total_floor = forms.IntegerField(required=False, label='Этажей всего',
                                           widget=forms.NumberInput(attrs={
                                               'class': 'form-control',
                                               'placeholder': 'Этажей всего',
                                               'data-select': '#sampleSelect',
                                               'data-option': 'house',
                                               'attribute': 'hidden',
                                               'min': '0',
                                               'max': '99'
                                           }))
    com_total_floor = forms.IntegerField(required=False, label='Этажей всего',
                                         widget=forms.NumberInput(attrs={
                                             'class': 'form-control',
                                             'placeholder': 'Этажей всего',
                                             'data-select': '#sampleSelect',
                                             'data-option': 'com',
                                             'attribute': 'hidden',
                                             'min': '0',
                                             'max': '99'
                                         }))
    flat_material = forms.ModelChoiceField(required=False, queryset=MaterialChoices.objects.all(), label='Материал стен',
                                    widget=forms.Select(attrs={
                                        'class': 'form-select',
                                        'placeholder': 'Материал стен',
                                        'data-select': '#sampleSelect',
                                        'data-option': 'flat',
                                        'attribute': 'hidden'
                                    }))
    house_material = forms.ModelChoiceField(required=False, queryset=MaterialChoices.objects.all(), label='Материал стен',
                                     widget=forms.Select(attrs={
                                         'class': 'form-select',
                                         'placeholder': 'Материал стен',
                                         'data-select': '#sampleSelect',
                                         'data-option': 'house',
                                         'attribute': 'hidden'
                                     }))
    garage_material = forms.ModelChoiceField(required=False, queryset=MaterialChoices.objects.all(), label='Материал стен',
                                      widget=forms.Select(attrs={
                                          'class': 'form-select',
                                          'placeholder': 'Материал стен',
                                          'data-select': '#sampleSelect',
                                          'data-option': 'garage',
                                          'attribute': 'hidden'
                                      }))
    com_material = forms.ModelChoiceField(required=False, queryset=MaterialChoices.objects.all(), label='Материал стен',
                                   widget=forms.Select(attrs={
                                       'class': 'form-select',
                                       'placeholder': 'Материал стен',
                                       'data-select': '#sampleSelect',
                                       'data-option': 'com',
                                       'attribute': 'hidden'
                                   }))
    flat_livin_surface = forms.FloatField(required=False, label='Жилая площадь',
                                          widget=forms.NumberInput(attrs={
                                              'class': 'form-control',
                                              'placeholder': 'Жилая площадь',
                                              'data-select': '#sampleSelect',
                                              'data-option': 'flat',
                                              'attribute': 'hidden',
                                              'min': '0',
                                              'step': "0.01"
                                          }))
    house_livin_surface = forms.FloatField(required=False, label='Жилая площадь',
                                           widget=forms.NumberInput(attrs={
                                               'class': 'form-control',
                                               'placeholder': 'Жилая площадь',
                                               'data-select': '#sampleSelect',
                                               'data-option': 'house',
                                               'attribute': 'hidden',
                                               'min': '0',
                                               'step': "0.01"
                                           }))
    buy_price = forms.CharField(required=False, label='Цена',
                                widget=forms.TextInput(attrs={
                                    'class': 'price form-control',
                                    'placeholder': 'Цена',
                                    'data-select': '#sampleSelect2',
                                    'data-option': 'buy',
                                    'attribute': 'hidden',
                                }))
    sell_price = forms.CharField(required=False, label='Жилая площадь',
                                 widget=forms.TextInput(attrs={
                                     'class': 'price form-control',
                                     'placeholder': 'Цена',
                                     'data-select': '#sampleSelect2',
                                     'data-option': 'sell',
                                     'attribute': 'hidden',
                                 }))
    rent_price = forms.CharField(required=False, label='Жилая площадь',
                                 widget=forms.TextInput(attrs={
                                     'class': 'price form-control',
                                     'placeholder': 'Цена',
                                     'data-select': '#sampleSelect2',
                                     'data-option': 'rent',
                                     'attribute': 'hidden',
                                 }))
    take_price = forms.CharField(required=False, label='Жилая площадь',
                                 widget=forms.TextInput(attrs={
                                     'class': 'price form-control',
                                     'placeholder': 'Цена',
                                     'data-select': '#sampleSelect2',
                                     'data-option': 'take',
                                     'attribute': 'hidden',
                                 }))

    class Meta:
        model = Item
        fields = ['type', 'item_type', 'phone_number', 'region', 'sub_region', 'city',
                  'street', 'trade', 'description', 'total_surface', 'name']

    def clean(self):
        cleaned_data = super().clean()
        type = self.cleaned_data['type']
        data = self.cleaned_data[f'{type}_price'].replace(' ', '')

        if not data.isdigit():
            raise ValidationError("В строке стоимость должны быть только цифры")

        return cleaned_data

    def __init__(self, *args, **kwargs):
        super(ItemForm, self).__init__(*args, **kwargs)

        for field in self.fields:
            if field == 'phone_number':
                self.fields[f'{field}'].error_messages = {'invalid': 'Телефон заполнен некорректно'}
            else:
                label = self.fields[f'{field}'].label
                self.fields[f'{field}'].error_messages = {'invalid': f'Вы не заполнили поле {label}'}

        self.fields['region'].widget.attrs \
            .update({
            'class': 'form-control region-select',
        })
        self.fields['sub_region'].widget.attrs \
            .update({
            'class': 'form-control region-select',
        })
        self.fields['type'].widget.attrs \
            .update({
            'class': 'form-control',
            'id': 'sampleSelect2'
        })

        self.fields['item_type'].widget.attrs \
            .update({
            'id': 'sampleSelect',
            'class': 'form-select mb-3'
        })

        self.fields['city'].widget.attrs \
            .update({
            'class': 'form-control',
            'placeholder': 'Город'
        })

        self.fields['street'].widget.attrs \
            .update({
            'class': 'form-control',
            'placeholder': 'Улица'
        })

        self.fields['phone_number'].widget.attrs \
            .update({
            'class': 'form-control',
            'value': '+7',
            'placeholder': 'Номер телефона',
            'maxlength': "12"

        })

        self.fields['trade'].widget.attrs \
            .update({
            'class': 'form-checkbox-control',
        })

        self.fields['description'].widget.attrs \
            .update({
            'class': 'form-control',
            'style': 'height: 100px',
            'placeholder': 'Описание'
        })
        self.fields['total_surface'].widget.attrs \
            .update({
            'placeholder': 'Общая площадь',
            'class': 'form-control',
            'min': '0',
            'step': "0.01"
        })
        self.fields['name'].widget.attrs \
            .update({
            'placeholder': 'Основное название',
            'class': 'form-control',
        })


class ImageForm(forms.ModelForm):
    image = forms.ImageField(required=False, widget=forms.FileInput(attrs={
        'class': 'bird-form form-control form-control-img',
        'onchange': "showFile(this)",
    }))

    class Meta:
        model = Images
        fields = ('image',)
