from django import forms
from .models import Item, Images
from items_window.handler import material_choices


class ItemForm(forms.ModelForm):
    com_floor = forms.IntegerField(required=False, label='Этаж',

                                   widget=forms.NumberInput(attrs={
                                       'class': 'form-control',
                                       'placeholder': 'Этаж',
                                       'data-select': '#sampleSelect',
                                       'data-option': 'com',
                                       'attribute': 'hidden',
                                       'min': '0'
                                   }))
    flat_floor = forms.IntegerField(required=False, label='Этаж',
                                    widget=forms.NumberInput(attrs={
                                        'class': 'form-control',
                                        'placeholder': 'Этаж',
                                        'data-select': '#sampleSelect',
                                        'data-option': 'flat',
                                        'attribute': 'hidden',
                                        'min': '0'
                                    }))

    house_total_floor = forms.IntegerField(required=False, label='Этажей всего',
                                           widget=forms.NumberInput(attrs={
                                               'class': 'form-control',
                                               'placeholder': 'Этажей всего',
                                               'data-select': '#sampleSelect',
                                               'data-option': 'house',
                                               'attribute': 'hidden',
                                               'min': '0'
                                           }))
    com_total_floor = forms.IntegerField(required=False, label='Этажей всего',
                                         widget=forms.NumberInput(attrs={
                                             'class': 'form-control',
                                             'placeholder': 'Этажей всего',
                                             'data-select': '#sampleSelect',
                                             'data-option': 'com',
                                             'attribute': 'hidden',
                                             'min': '0'
                                         }))
    flat_material = forms.CharField(required=False, max_length=50, label='Материал стен',
                                    widget=forms.Select(attrs={
                                        'class': 'form-select',
                                        'placeholder': 'Материал стен',
                                        'data-select': '#sampleSelect',
                                        'data-option': 'flat',
                                        'attribute': 'hidden'
                                    }, choices=material_choices))
    house_material = forms.CharField(required=False, max_length=50, label='Материал стен',
                                     widget=forms.Select(attrs={
                                         'class': 'form-select',
                                         'placeholder': 'Материал стен',
                                         'data-select': '#sampleSelect',
                                         'data-option': 'house',
                                         'attribute': 'hidden'
                                     }, choices=material_choices))
    garage_material = forms.CharField(required=False, max_length=50, label='Материал стен',
                                      widget=forms.Select(attrs={
                                          'class': 'form-select',
                                          'placeholder': 'Материал стен',
                                          'data-select': '#sampleSelect',
                                          'data-option': 'garage',
                                          'attribute': 'hidden'
                                      }, choices=material_choices))
    com_material = forms.CharField(required=False, max_length=50, label='Материал стен',
                                   widget=forms.Select(attrs={
                                       'class': 'form-select',
                                       'placeholder': 'Материал стен',
                                       'data-select': '#sampleSelect',
                                       'data-option': 'com',
                                       'attribute': 'hidden'
                                   }, choices=material_choices))
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

    class Meta:
        model = Item
        fields = ['type', 'item_type', 'phone_number', 'region', 'city',
                  'street', 'trade', 'price', 'description', 'total_surface']

    def __init__(self, *args, **kwargs):
        super(ItemForm, self).__init__(*args, **kwargs)
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

        self.fields['region'].widget.attrs \
            .update({
            'class': 'form-select mb-3',

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
            'placeholder': 'Номер телефона'

        })

        self.fields['trade'].widget.attrs \
            .update({
            'class': 'form-check-input',
        })

        self.fields['price'].widget.attrs \
            .update({
            'class': 'form-control',
            'placeholder': 'Цена',
            'min': '0'
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


class ImageForm(forms.ModelForm):
    image = forms.ImageField(widget=forms.FileInput(attrs={
        'class': 'bird-form form-control form-control-img'
    }))

    class Meta:
        model = Images
        fields = ('image',)
