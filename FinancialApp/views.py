import time

from django.db import connection
from django.shortcuts import render, redirect
import django.db.utils
import FinancialApp.forms
import FinancialApp.models
from django.utils.timezone import now


# Create your views here.
def index(request):
    context = {}
    if is_login(request):
        context['login'] = request.session['login']
    else:
        context['login'] = 'Anon'
    return render(request, 'index.html', context)


def change_profile_data(request):
    context = {}
    error = False
    context['error'] = error

    if request.method == 'POST':
        form = FinancialApp.forms.ChangeUserData(request.POST)

        if form.is_valid():
            id = get_user_id(request)
            password = form.data['Password']
            email = form.data['Email']
            name = form.data['Name']
            surname = form.data['Surname']
            if password != '':
                with connection.cursor() as cursor:
                    cursor.execute('UPDATE FinancialApp_users SET Password=%s WHERE id==%s', [password, id])
            if email != '':
                with connection.cursor() as cursor:
                    cursor.execute('UPDATE FinancialApp_users SET Email=%s WHERE id==%s', [email, id])
            if name != '':
                with connection.cursor() as cursor:
                    cursor.execute('UPDATE FinancialApp_users SET Name=%s WHERE id==%s', [name, id])
            if surname != '':
                with connection.cursor() as cursor:
                    cursor.execute('UPDATE FinancialApp_users SET Surname=%s WHERE id==%s', [surname, id])
            return redirect('/profile/')

    form = FinancialApp.forms.ChangeUserData()
    context['form'] = form

    return render(request, 'change.html', context)


def get_profile_data(id):
    with connection.cursor() as cursor:
        data = cursor.execute('SELECT * FROM FinancialApp_users WHERE id==%s', [id]).fetchone()
    dict_data = []
    for i in range(len(data)):
        dict_data.append((cursor.description[i][0], data[i]))
    return dict_data


def profile(request):
    if is_login(request):
        context = {}
        error = False
        context['error'] = error

        id = get_user_id(request)

        if request.method == 'POST':
            form = FinancialApp.forms.UserAvatar(request.POST, request.FILES)
            if form.is_valid():
                user = FinancialApp.models.Users.objects.get(id=get_user_id(request))
                user.Avatar = request.FILES['Avatar']
                user.save()
                return redirect('/profile/')

        form = FinancialApp.forms.UserAvatar()
        context['form'] = form

        data = get_profile_data(id)
        context['data'] = data

        return render(request, 'profile.html', context)
    else:
        return redirect('/login')


def diary(request):
    if is_login(request):
        context = {}
        error = False

        user_id = get_user_id(request)
        with connection.cursor() as cursor:
            transaction_dates = cursor.execute(
                'SELECT CurrentAmount, Date FROM FinancialApp_statistics WHERE UserID==%s', [user_id]).fetchall()
            cur_amount = cursor.execute('SELECT Amount FROM FinancialApp_users WHERE id==%s', [user_id]).fetchone()[0]
        new_transaction_dates = []
        for i in range(len(transaction_dates)):
            new_transaction_dates.append(
                [transaction_dates[i][0], int(time.mktime(transaction_dates[i][1].timetuple())) * 1000])
        try:
            first_log = new_transaction_dates[0][1]
            last_log = new_transaction_dates[-1][1]
        except IndexError:
            first_log = int(time.time())
            last_log = int(time.time())

        if request.method == 'POST':
            if 'Transaction' in request.POST:
                Transaction = FinancialApp.forms.Transaction(request.POST, prefix='Transaction')
                if Transaction.is_valid():
                    if 'Plus' in Transaction.data:
                        amount = abs(int(Transaction.data['Transaction-Amount']))
                        cur_amount += amount
                        with connection.cursor() as cursor:
                            cursor.execute(
                                'INSERT INTO FinancialApp_statistics(UserID, CurrentAmount, Amount, Category, Date) VALUES(%s, %s, %s, %s, %s)',
                                [user_id, cur_amount, amount, 'Зарплата', now()])
                    else:
                        amount = -1 * abs(int(Transaction.data['Transaction-Amount']))
                        cur_amount += amount
                        with connection.cursor() as cursor:
                            cursor.execute(
                                'INSERT INTO FinancialApp_statistics(UserID, CurrentAmount, Amount, Category, Date) VALUES(%s, %s, %s, %s, %s)',
                                [user_id, cur_amount, amount, 'Трата', now()])
                    with connection.cursor() as cursor:
                        cursor.execute('UPDATE FinancialApp_users SET Amount = Amount + %s WHERE id == %s',
                                       [amount, user_id])
            return redirect('/diary')

        table = get_transaction_table(user_id)
        Transaction = FinancialApp.forms.Transaction(prefix='Transaction')

        context['date'] = [first_log, last_log, new_transaction_dates]
        context['amount'] = cur_amount
        context['table'] = table
        context['Transaction'] = Transaction
        context['error'] = error

        return render(request, 'diary.html', context)
    else:
        return redirect('/login/')


def register(request):
    if not is_login(request):
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
                        data.save()
                        return redirect('/login/')
                    except django.db.utils.IntegrityError:
                        error = True

        form = FinancialApp.forms.Register()
        context['error'] = error
        context['form'] = form
        return render(request, 'register.html', context)
    else:
        return redirect('/')


def login(request):
    if not is_login(request):
        context = {}
        error = False
        if request.method == 'POST':
            form = FinancialApp.forms.Login(request.POST)

            if form.is_valid():
                login = form.data['Login']
                password = form.data['Password']
                with connection.cursor() as cursor:
                    data = cursor.execute(
                        'SELECT Login, Password FROM FinancialApp_users WHERE Login==%s AND Password==%s',
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
    else:
        return redirect('/')


def logout(request):
    if is_login(request):
        del request.session['login']
    return redirect('/')


def is_login(request):
    if request.session.get('login') is None:
        return False
    return True


def get_user_id(request):
    login = request.session['login']
    with connection.cursor() as cursor:
        user_id = cursor.execute('SELECT id FROM FinancialApp_users WHERE Login==%s', [login]).fetchone()[0]
    return user_id


def get_transaction_table(user_id):
    with connection.cursor() as cursor:
        data = cursor.execute('SELECT Amount, Category, Date FROM FinancialApp_statistics WHERE UserID == %s',
                              [user_id]).fetchall()

    return data


def table(request):
    if is_login(request):
        context = {}
        error = False
        id = get_user_id(request)
        with connection.cursor() as cursor:
            amount = cursor.execute('SELECT Amount FROM FinancialApp_users WHERE id == %s', [id]).fetchone()[0]
        context['amount'] = amount
        return render(request, 'table.html', context)
    else:
        return redirect('/login')
