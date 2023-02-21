from django import forms
from .models import FeedBack, Report


class FeedBackForm(forms.ModelForm):

    class Meta:
        model = FeedBack
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        super(FeedBackForm, self).__init__(*args, **kwargs)

        for field in self.fields:
            if field == 'phone_number':
                self.fields[f'{field}'].error_messages = {'invalid': 'Телефон заполнен некорректно'}
            else:
                label = self.fields[f'{field}'].label
                self.fields[f'{field}'].error_messages = {'invalid': f'Вы не заполнили поле {label}'}

        self.fields['phone_number'].widget.attrs \
            .update({
            'class': 'form-control',
            'placeholder': 'Введите номер телефона (+7...)',
            'maxlength': "12",
            'value': '+7',
        })

        self.fields['email'].widget.attrs \
            .update({
            'class': 'form-control',
            'placeholder': 'Электронная почта',
        })

        self.fields['text'].widget.attrs \
            .update({
            'class': 'form-control',
            'rows': '5',
            'placeholder': 'Введите текст',
        })


class ReportForm(forms.ModelForm):
    class Meta:
        model = Report
        fields = ['reason', 'report_text']

    def __init__(self, *args, **kwargs):
        super(ReportForm, self).__init__(*args, **kwargs)

        self.fields['report_text'].widget.attrs \
            .update({
            'class': 'form-control',
            'placeholder': 'Комментарий',
            'row': "3",
            'style': 'width: 40rem; margin-left: -3.5%',
        })

        self.fields['reason'].widget.attrs \
            .update({
            'class': 'form-control',
            'style': 'width: 150px; margin: 1.5%;'

        })