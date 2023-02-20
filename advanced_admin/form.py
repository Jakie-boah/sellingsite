from django import forms
from handlers.models import BlackList


class AddForm(forms.ModelForm):
    class Meta:
        model = BlackList
        fields = '__all__'
