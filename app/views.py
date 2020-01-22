from django.shortcuts import render
import datetime


def home(request):
    context = {
        'date': datetime.date.today(),
    }
    return render(request, "home.html", context)


def login(request):
    return render(request, "login.html")


def register(request):
    return render(request,"register.html")