from django import forms


class SignInForm(forms.Form):
    username = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Your username'}), label=False)
    password = forms.CharField(widget=forms.PasswordInput(attrs={'placeholder': 'Your password'}), label=False)
    remember_me = forms.BooleanField(label='Remember Me', label_suffix='', required=False)


class SignUpForm(forms.Form):
    email = forms.EmailField(widget=forms.EmailInput(attrs={'placeholder': 'Your email'}), label=False)
    username = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Your username'}), label=False)
    password = forms.CharField(widget=forms.PasswordInput(attrs={'placeholder': 'Your password'}), label=False)
    repeat_password = forms.CharField(widget=forms.PasswordInput(attrs={'placeholder': 'Repeat password'}), label=False)
    agree_rules = forms.BooleanField(label='I agree with with site\'s Terms of Services', label_suffix='',
                                     required=True, widget=forms.CheckboxInput())
