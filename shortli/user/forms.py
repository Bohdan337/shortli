from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm



class SignUpForm(UserCreationForm):
    username = forms.CharField(
        widget=forms.TextInput(attrs={
            'placeholder': 'Username',
        }),
        help_text='',
        label=''
    )

    email = forms.EmailField(required=True, widget=forms.EmailInput(attrs={
            'placeholder': 'Email@gmail.com',
        }),
        help_text='', 
        label=''   )
    password1 = forms.CharField(
        widget=forms.PasswordInput(attrs={
            'placeholder': 'Password',
        }),
        help_text='', 
        label=''       
    )

    password2 = forms.CharField(
        widget=forms.PasswordInput(attrs={
            'placeholder': 'Password confirmation',
        }),
        help_text='', 
        label=''       
    )
    
    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']

class LoginForm(forms.Form):
    username = forms.CharField(max_length=150, label='', widget=forms.TextInput(attrs={
            'placeholder': 'Username ',
            'style': 'color: #D9D9D9; font-size: 12px;'
        }))
    password = forms.CharField(label='', widget=forms.PasswordInput(attrs={
            'placeholder': 'Password'
        }))


