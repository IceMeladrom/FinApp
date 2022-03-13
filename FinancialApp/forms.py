from django import forms
import datetime as dt

# Create your forms here.


class Register(forms.Form):
    Login = forms.CharField(label='Введите логин', min_length=4, max_length=64)
    Password = forms.CharField(label='Введите пароль', min_length=5, widget=forms.PasswordInput)
    ConfirmPassword = forms.CharField(label='Введите пароль еще раз', min_length=5, widget=forms.PasswordInput)
    Email = forms.EmailField(label='Введите эл. почту')
    Name = forms.CharField(label="Введите имя")
    Surname = forms.CharField(label="Введите фамилию")


class Login(forms.Form):
    Login = forms.CharField(label='Введите логин', min_length=4, max_length=64)
    Password = forms.CharField(label='Введите пароль', min_length=5, widget=forms.PasswordInput)


class Transaction(forms.Form):
    Amount = forms.IntegerField(label='Введите сумму', required=False)


class ChangeUserData(forms.Form):
    Password = forms.CharField(label='Введите новый пароль', min_length=5, widget=forms.PasswordInput, required=False)
    Email = forms.EmailField(label='Введите новую почту', required=False)
    Name = forms.CharField(label='Введите новое имя', required=False)
    Surname = forms.CharField(label='Введите новую фамилию', required=False)


class UserAvatar(forms.Form):
    Avatar = forms.ImageField(label='Загрузите аватарку')
