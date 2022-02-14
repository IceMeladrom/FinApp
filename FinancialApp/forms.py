from django import forms


# Create your forms here.
class SignUp(forms.Form):
    Login = forms.CharField(label='Введите логин', min_length=4, max_length=64)
    Password = forms.CharField(label='Введите пароль', min_length=5, widget=forms.PasswordInput)
    ConfirmPassword = forms.CharField(label='Введите пароль еще раз', min_length=5, widget=forms.PasswordInput)
    Email = forms.EmailField(label='Введите эл. почту')
    Name = forms.CharField(label="Введите имя")
    Surname = forms.CharField(label="Введите фамилию")


class SignIn(forms.Form):
    Login = forms.CharField(label='Введите логин', min_length=4, max_length=64)
    Password = forms.CharField(label='Введите пароль', min_length=5, widget=forms.PasswordInput)
