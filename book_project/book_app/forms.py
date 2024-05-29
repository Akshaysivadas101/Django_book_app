from django import forms
from .models import Book, Author
from django.contrib.auth.forms import UserCreationForm,AuthenticationForm
from django.contrib.auth.models import User

class BookForm(forms.ModelForm):
    class Meta:
        model = Book
        fields = '__all__'
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter the book name'}),
            'price': forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Enter the book price'}),
            'author': forms.Select(attrs={'class': 'form-control', 'placeholder': 'Enter the author name'}),
        }

class AuthorForm(forms.ModelForm):
    class Meta:
        model = Author
        fields = ['name']

class RegisterForm(UserCreationForm):
    email = forms.EmailField(required=True)
    class Meta:
        model = User
        fields = ['username','email','password1','password2']


class LoginForm(AuthenticationForm):
    username = forms.CharField(label='Username', max_length=150)
    password = forms.CharField(label='Password', widget=forms.PasswordInput)

    def __init__(self, *args, **kwargs):
        super(LoginForm, self).__init__(*args, **kwargs)
        self.fields['username'].label = 'Username'
        self.fields['password'].label = 'Password'
