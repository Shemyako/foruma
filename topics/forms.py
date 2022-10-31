from django import forms

class SendingMessageForm(forms.Form):
    text = forms.CharField()


class AuthForm(forms.Form):
    login = forms.CharField()
    password = forms.CharField()