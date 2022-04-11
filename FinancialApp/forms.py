from django import forms
import datetime as dt


# Create your forms here.


class Register(forms.Form):
    Login = forms.CharField(label='Введите логин', min_length=4, max_length=64,
                            widget=forms.TextInput(attrs={'class': 'form-control'}))
    Password = forms.CharField(label='Введите пароль', min_length=5,
                               widget=forms.PasswordInput(attrs={'class': 'form-control'}))
    ConfirmPassword = forms.CharField(label='Введите пароль еще раз', min_length=5,
                                      widget=forms.PasswordInput(attrs={'class': 'form-control'}))
    Email = forms.EmailField(label='Введите эл. почту', widget=forms.EmailInput(attrs={'class': 'form-control'}))
    Name = forms.CharField(label="Введите имя", widget=forms.TextInput(attrs={'class': 'form-control'}))
    Surname = forms.CharField(label="Введите фамилию", widget=forms.TextInput(attrs={'class': 'form-control'}))


class Login(forms.Form):
    Login = forms.CharField(label='Введите логин', min_length=4, max_length=64,
                            widget=forms.TextInput(attrs={'class': 'form-control'}))
    Password = forms.CharField(label='Введите пароль', min_length=5,
                               widget=forms.PasswordInput(attrs={'class': 'form-control'}))


class Transaction(forms.Form):
    Amount = forms.IntegerField(label='Введите сумму', required=False,
                                widget=forms.NumberInput(attrs={'class': 'form-control'}))


class CostCategory(forms.Form):
    Category = forms.CharField(label='Введите категорию', required=False,
                               widget=forms.TextInput(attrs={'class': 'form-control'}))


class ChangeUserData(forms.Form):
    Password = forms.CharField(label='Введите новый пароль', min_length=5,
                               widget=forms.PasswordInput(attrs={'class': 'form-control'}), required=False)
    Email = forms.EmailField(label='Введите новую почту', required=False,
                             widget=forms.EmailInput(attrs={'class': 'form-control'}))
    Name = forms.CharField(label='Введите новое имя', required=False,
                           widget=forms.TextInput(attrs={'class': 'form-control'}))
    Surname = forms.CharField(label='Введите новую фамилию', required=False,
                              widget=forms.TextInput(attrs={'class': 'form-control'}))


class UserAvatar(forms.Form):
    Avatar = forms.ImageField(label='Загрузите аватарку', widget=forms.FileInput(attrs={'class': 'form-control'}))


class Article(forms.Form):
    Name = forms.CharField(label='Название статьи', widget=forms.TextInput(attrs={'placeholder': 'Название статьи', 'class': 'form-control'}))
    Text = forms.CharField(label='Текст статьи', widget=forms.Textarea(attrs={'placeholder': 'Текст статьи', 'class': 'form-control'}))
