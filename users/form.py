from .models import UserProfile, Comments, Favourites
from django import forms
from phonenumber_field.formfields import PhoneNumberField
from django.core.exceptions import ValidationError


class UserForm(forms.ModelForm):
    phone_number = PhoneNumberField(required=False, label='Номер телефона',
                                    widget=forms.TextInput(attrs={'placeholder': '+7()..',
                                                                  'class': 'form-control regist-input',
                                                                  'maxlength': "12"}))
    username = forms.CharField(max_length=50, label='Имя', required=False,
                               widget=forms.TextInput(attrs={'placeholder': 'Имя',
                                                             'class': 'form-control regist-input',
                                                             'maxlength': "50"}))
    usersurname = forms.CharField(max_length=50, label='Фамилия', required=False,
                                  widget=forms.TextInput(attrs={'placeholder': 'Фамилия',
                                                                'class': 'form-control regist-input',
                                                                'maxlength': "50"}))
    email = forms.EmailField(error_messages={'invalid': "Допустили ошибку в email"},
                             widget=forms.EmailInput(attrs={'placeholder': 'Адрес почты',
                                                            'class': 'form-control regist-input'}))

    phone_number.error_messages['invalid'] = 'Некорректно введен номер телефона'

    class Meta:
        model = UserProfile
        fields = ['phone_number', 'username', 'usersurname', 'email']

    def clean_phone_number(self):
        phone_number = self.cleaned_data.get('phone_number')
        if not phone_number:
            raise ValidationError('Вы должны заполнить поля!')
        return phone_number

    def clean_name(self):
        name = self.cleaned_data.get('name')
        if not name:
            raise ValidationError('Вы должны заполнить поля!')
        return name

    def clean_usersurname(self):
        usersurname = self.cleaned_data.get('usersurname')
        if not usersurname:
            raise ValidationError('Вы должны заполнить поля!')
        return usersurname

    def clean_email(self):
        email = self.cleaned_data.get('email')
        if not email:
            raise ValidationError('Вы должны заполнить поля!')
        return email


class LoginForm(forms.Form):
    login = PhoneNumberField(required=False, label='Номер телефона',
                             widget=forms.TextInput(attrs={'placeholder': '+7()..',
                                                           'class': 'form-control regist-input',
                                                           'maxlength': "12"}))
    password = forms.CharField(required=False,
                               widget=forms.PasswordInput(attrs={'placeholder': 'Пароль',
                                                                 'class': 'form-control regist-input',
                                                                 'maxlength': "7"}))

    def clean_login(self):
        login = self.cleaned_data.get('login')
        if not login:
            raise ValidationError('Вы должны заполнить поля!')
        return login

    def clean_password(self):
        password = self.cleaned_data.get('password')
        if not password:
            raise ValidationError('Вы должны заполнить поля!')
        return password


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comments
        fields = ['text']

    def __init__(self, *args, **kwargs):
        super(CommentForm, self).__init__(*args, **kwargs)

        self.fields['text'].widget.attrs \
            .update({
            'class': 'form-control',
            'placeholder': 'Комментарий',
            'row': '3',
            'id': 'csbmtend'
        })


class FavouriteForm(forms.ModelForm):
    class Meta:
        model = Favourites
        fields = ['name']

    def __init__(self, *args, **kwargs):
        super(FavouriteForm, self).__init__(*args, **kwargs)
        self.fields['name'].widget.attrs \
            .update({
            'name': 'fav_type',
            'placeholder': 'Охарактеризуйте тип этого объявления (можно оставить пустым)',
            'rows': '3',
            'style': 'margin-left: -3%; width: 20rem;'
        })
