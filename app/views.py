from django.shortcuts import render
from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import HttpResponseRedirect
from django.urls import reverse
from app.models import AppUser
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
    context = dict()
    form = UserCreationForm(request.POST)
    if form.is_valid():
        new_user = form.save()
        email = request.POST['email']
        first_name = request.POST['fname']
        last_name = request.POST['lname']
        new_user.first_name = first_name
        new_user.last_name = last_name
        new_user.email = email
        new_user.save()
        acct_holder = AppUser(user=new_user)
        acct_holder.points = 1000
        acct_holder.save()
        return HttpResponseRedirect(reverse("login"))
    else:
        form = UserCreationForm()
        context['form'] = form
        return render(request, "registration/register.html", context)


def loggedIn(request):
    data = dict()
    return render(request, 'loggedIn.html', context=data)


def guest(request):
    return render(request, 'guest.html')

def process_guest(request):
    try:
        name = request.GET['user_name']
        dob = request.GET['dob']
        email = request.GET['email']
    except:
        return render(request, 'guest.html')
    try:
        request.GET['cancel']
        return home(request)
    except:
        pass
    import datetime
    today = datetime.date.today()
    then = datetime.datetime.strptime(dob,"%Y-%m-%d")
    print(today, then)
    diff = today-then.date()
    context = dict()
    context['name'] = name
    context['dob'] = dob
    context['age'] = diff.days
    return render(request, 'guest_result.html', context=context)

