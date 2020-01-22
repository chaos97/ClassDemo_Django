from django.shortcuts import render
import datetime


def home(request):
    context = {
        'date': datetime.date.today(),
        'persons': [['John', 'New York'], ['Mary', 'Boston']],
    }
    return render(request, "home.html", context)


def login(request):
    return render(request, "registration/login.html")


def register(request):
    return render(request,"register.html")


def loggedIn(request):
    data = dict()
    return render(request, 'loggedIn.html', context=data)