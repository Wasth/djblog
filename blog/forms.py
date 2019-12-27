from django import forms
from django_summernote.widgets import SummernoteWidget
from blog.models import Post


class SignInForm(forms.Form):
    username = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Your username'}), label=False)
    password = forms.CharField(widget=forms.PasswordInput(attrs={'placeholder': 'Your password'}), label=False)
    remember_me = forms.BooleanField(label='Remember Me', label_suffix='', required=False)


class CreatePostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['title', 'anons', 'text', 'image', 'category', 'tag']
        widgets = {
            'title': forms.TextInput(attrs={'placeholder': 'Title'}),
            'anons': forms.TextInput(attrs={'placeholder': 'Short text of post(anons)'}),
            'text': SummernoteWidget(),
            # 'text': forms.Textarea(attrs={'placeholder': 'Text of post'}),

        }
        labels = {
            'title': False,
            'anons': False,
            'text': False,
        }


class SignUpForm(forms.Form):
    email = forms.EmailField(widget=forms.EmailInput(attrs={'placeholder': 'Your email'}),
                             label=False)
    username = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Your username'}),
                               label=False,
                               min_length=3)
    password = forms.CharField(widget=forms.PasswordInput(attrs={'placeholder': 'Your password'}),
                               label=False,
                               min_length=6)
    repeat_password = forms.CharField(widget=forms.PasswordInput(attrs={'placeholder': 'Repeat password'}),
                                      label=False)
    agree_rules = forms.BooleanField(label='I agree with with site\'s Terms of Services',
                                     label_suffix='',
                                     required=True,
                                     widget=forms.CheckboxInput())

    def clean(self):
        cleaned_data = super(SignUpForm, self).clean()
        password = cleaned_data.get("password")
        confirm_password = cleaned_data.get("repeat_password")

        if password != confirm_password:
            self.add_error('repeat_password', 'Password and repeated password must match')
