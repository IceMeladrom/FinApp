from django.db import connection
from django.shortcuts import render, redirect
import django.db.utils
import FinancialApp.forms
import FinancialApp.models


# Create your views here.
def index(request):
    return render(request, 'index.html')


def register(request):
    context = {}
    error = False
    if request.method == 'POST':
        form = FinancialApp.forms.Register(request.POST)

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
                    data = FinancialApp.models.Users(Login=login, Password=password, Email=email, Name=name,
                                                     Surname=surname)
                except django.db.utils.IntegrityError:
                    error = True

    form = FinancialApp.forms.Register()
    context['error'] = error
    context['form'] = form
    return render(request, 'register.html', context)


def login(request):
    context = {}
    error = False
    if request.method == 'POST':
        form = FinancialApp.forms.Login(request.POST)

        if form.is_valid():
            login = form.data['Login']
            password = form.data['Password']
            with connection.cursor() as cursor:
                data = cursor.execute('SELECT Login, Password FROM FinancialApp_users WHERE Login==%s AND Password==%s',
                                      [login, password]).fetchone()
            if data is None:
                error = True
            else:
                request.session['login'] = login
                return redirect('/')

    form = FinancialApp.forms.Login()
    context['form'] = form
    context['error'] = error
    return render(request, 'login.html', context)
