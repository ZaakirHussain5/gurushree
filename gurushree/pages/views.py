from django.shortcuts import render


def index(request):
    return render(request, 'auth/index.html')


def login(request):
    return render(request, 'auth/login.html')


def dashboard(request):
    return render(request, 'auth/dashboard.html')


def departments(request):
    return render(request, 'masters/departments.html')


def places(request):
    return render(request, 'masters/places.html')


def regTypes(request):
    return render(request, 'masters/regTypes.html')


def generals(request):
    return render(request, 'masters/generals.html')


def incomeExpenses(request):
    return render(request, 'masters/incomeExpenses.html')


def menus(request):
    return render(request, 'masters/menus.html')


def pages(request):
    return render(request, 'masters/pages.html')


def hospitals(request):
    return render(request, 'masters/hospitals.html')


def users(request):
    return render(request, 'masters/users.html')


def professionals(request):
    return render(request, 'masters/professionals.html')

def genTypes(request):
    return render(request,'masters/genTypes.html')


def disType(request):
    return render(request,'masters/disTypes.html')
