from django import forms
from django.core.exceptions import ValidationError
from django.utils.translation import gettext_lazy as _
from .models import Users#, Topics, Messages
from .auth import check_password

class SendingMessageForm(forms.Form):
    text = forms.CharField()


class AuthForm(forms.Form):
    login = forms.CharField()
    password = forms.CharField()
    def clean(self):
        data = super().clean()
        if 'login' not in data or 'password' not in data:
            raise ValidationError('Такого аккаунта не существует')

        login_to_check = data.get('login')
        password_to_check = data.get('password')
        user = Users.objects.filter(name=login_to_check)

        if not user:
            raise ValidationError('Такого аккаунта не существует')
        elif not check_password(password_to_check, user[0].password):
            raise ValidationError('Такого аккаунта не существует')
        return {"login":login_to_check, "password": password_to_check}
        


class SignUpForm(forms.Form):
    login = forms.CharField()
    password = forms.CharField()

    def clean_login(self):
        login_to_check = self.cleaned_data['login']

        if Users.objects.filter(name=login_to_check):
            raise ValidationError('Такой логин уже существует')
        return login_to_check