from django import forms
from .models import Item, Images


class ItemForm(forms.ModelForm):
    class Meta:
        model = Item
        fields = '__all__'

class ImageForm(forms.ModelForm):
    image = forms.ImageField(label='Image')
    class Meta:
        model = Images
        fields = ('image', )
