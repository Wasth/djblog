from django import forms


class SignInForm(forms.Form):
    username = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Your username'}), label=False)
    password = forms.CharField(widget=forms.PasswordInput(attrs={'placeholder': 'Your password'}), label=False)
    rememberMe = forms.BooleanField(label='Remember Me', label_suffix='')
