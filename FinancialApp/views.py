from django.db import connection
from django.shortcuts import render
import django.db.utils
import forms
import models


# Create your views here.
def index(request):
    return render(request, 'index.html')


def sign_up(request):
    context = {}
    error = False
    if request.method == 'POST':
        form = forms.SignUp(request.POST)

        if form.is_valid():
            login = form.data['Login']
            password = form.data['Password']
            confirmPassword = form.data['ConfirmPassword']
            email = form.data['Email']
            name = form.data['Name']
            surname = form.data['Surname']

            if password != confirmPassword:
                error = True
            else:
                try:
                    data = models.Users(Login=login, Password=password, Email=email, Name=name, Surname=surname)
                except django.db.utils.IntegrityError:
                    error = True

    form = forms.SignUp()
    context['error'] = error
    context['form'] = form
    return render(request, 'signup.html', context)


def sign_in(request):
    if request.method == 'POST':
        form = forms.SignUp(request.POST)

        if form.is_valid():
            login = form.data['Login']
            password = form.data['Password']
