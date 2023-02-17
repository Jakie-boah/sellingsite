from django import forms
from .models import Item, Images
from items_window.handler import material_choices


class ItemForm(forms.ModelForm):
    com_floor = forms.IntegerField(required=False, label='Этаж',
                                   error_messages={'invalid': 'Вы пропустили это поле'},
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
                                    error_messages={'invalid': 'Вы пропустили это поле'},
                                    widget=forms.NumberInput(attrs={
                                        'class': 'form-control',
                                        'placeholder': 'Этаж',
                                        'data-select': '#sampleSelect',
                                        'data-option': 'flat',
                                        'attribute': 'hidden',
                                        'min': '0',
                                        'max': '99'
                                    }))

    house_total_floor = forms.IntegerField(required=False, label='Этажей всего',
                                           error_messages={'invalid': 'Вы пропустили это поле'},
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
                                         error_messages={'invalid': 'Вы пропустили это поле'},
                                         widget=forms.NumberInput(attrs={
                                             'class': 'form-control',
                                             'placeholder': 'Этажей всего',
                                             'data-select': '#sampleSelect',
                                             'data-option': 'com',
                                             'attribute': 'hidden',
                                             'min': '0',
                                             'max': '99'
                                         }))
    flat_material = forms.CharField(required=False, max_length=50, label='Материал стен',
                                    error_messages={'invalid': 'Вы пропустили это поле'},
                                    widget=forms.Select(attrs={
                                        'class': 'form-select',
                                        'placeholder': 'Материал стен',
                                        'data-select': '#sampleSelect',
                                        'data-option': 'flat',
                                        'attribute': 'hidden'
                                    }, choices=material_choices))
    house_material = forms.CharField(required=False, max_length=50, label='Материал стен',
                                     error_messages={'invalid': 'Вы пропустили это поле'},
                                     widget=forms.Select(attrs={
                                         'class': 'form-select',
                                         'placeholder': 'Материал стен',
                                         'data-select': '#sampleSelect',
                                         'data-option': 'house',
                                         'attribute': 'hidden'
                                     }, choices=material_choices))
    garage_material = forms.CharField(required=False, max_length=50, label='Материал стен',
                                      error_messages={'invalid': 'Вы пропустили это поле'},
                                      widget=forms.Select(attrs={
                                          'class': 'form-select',
                                          'placeholder': 'Материал стен',
                                          'data-select': '#sampleSelect',
                                          'data-option': 'garage',
                                          'attribute': 'hidden'
                                      }, choices=material_choices))
    com_material = forms.CharField(required=False, max_length=50, label='Материал стен',
                                   error_messages={'invalid': 'Вы пропустили это поле'},
                                   widget=forms.Select(attrs={
                                       'class': 'form-select',
                                       'placeholder': 'Материал стен',
                                       'data-select': '#sampleSelect',
                                       'data-option': 'com',
                                       'attribute': 'hidden'
                                   }, choices=material_choices))
    flat_livin_surface = forms.FloatField(required=False, label='Жилая площадь',
                                          error_messages={'invalid': 'Вы пропустили это поле'},
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
                                           error_messages={'invalid': 'Вы пропустили это поле'},
                                           widget=forms.NumberInput(attrs={
                                                 'class': 'form-control',
                                                 'placeholder': 'Жилая площадь',
                                                 'data-select': '#sampleSelect',
                                                 'data-option': 'house',
                                                 'attribute': 'hidden',
                                                 'min': '0',
                                                 'step': "0.01"
                                             }))
    buy_price = forms.IntegerField(required=False, label='Жилая площадь',
                                   error_messages={'invalid': 'Вы пропустили это поле'},
                                   widget=forms.NumberInput(attrs={
                                        'class': 'price form-control',
                                        'placeholder': 'Цена',
                                        'min': '0',
                                        'data-select': '#sampleSelect2',
                                        'data-option': 'buy',
                                        'attribute': 'hidden',
                                    }))
    sell_price = forms.IntegerField(required=False, label='Жилая площадь',
                                    error_messages={'invalid': 'Вы пропустили это поле'},
                                    widget=forms.NumberInput(attrs={
                                       'class': 'price form-control',
                                       'placeholder': 'Цена',
                                       'min': '0',
                                       'data-select': '#sampleSelect2',
                                       'data-option': 'sell',
                                       'attribute': 'hidden',
                                   }))
    rent_price = forms.IntegerField(required=False, label='Жилая площадь',
                                    error_messages={'invalid': 'Вы пропустили это поле'},
                                    widget=forms.NumberInput(attrs={
                                        'class': 'price form-control',
                                        'placeholder': 'Цена',
                                        'min': '0',
                                        'data-select': '#sampleSelect2',
                                        'data-option': 'rent',
                                        'attribute': 'hidden',
                                    }))
    take_price = forms.IntegerField(required=False, label='Жилая площадь',
                                    error_messages={'invalid': 'Вы пропустили это поле'},
                                    widget=forms.NumberInput(attrs={
                                        'class': 'price form-control',
                                        'placeholder': 'Цена',
                                        'min': '0',
                                        'data-select': '#sampleSelect2',
                                        'data-option': 'take',
                                        'attribute': 'hidden',
                                    }))

    class Meta:
        model = Item
        fields = ['type', 'item_type', 'phone_number', 'region', 'city',
                  'street', 'trade', 'description', 'total_surface', 'name']

    def __init__(self, *args, **kwargs):
        super(ItemForm, self).__init__(*args, **kwargs)

        for field in self.fields:
            if field == 'phone_number':
                self.fields[f'{field}'].error_messages = {'invalid': 'Телефон заполнен некорректно'}
            else:
                self.fields[f'{field}'].error_messages = {'invalid': 'Не заполненное поле'}

        self.fields['region'].widget.attrs \
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


