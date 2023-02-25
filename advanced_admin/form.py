from django import forms
from handlers.models import BlackList


class AddForm(forms.ModelForm):
    class Meta:
        model = BlackList
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        super(AddForm, self).__init__(*args, **kwargs)
        self.fields['phone_number'].widget.attrs \
            .update({
            'class': 'form-control',
            'style': 'width: 315px;'
        })