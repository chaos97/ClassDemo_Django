"""project URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from app import views
from django.contrib import admin
from django.urls import path
from django.contrib.auth.views import LoginView

urlpatterns = [
    path('', views.home, name="home_url"),
    path('admin/', admin.site.urls),
    path('register/', views.register, name="register_url"),
    path('login/', LoginView.as_view(), name='login'),
    path('loggedIn/', views.loggedIn, name='loggedIn'),
    path('guest/', views.guest, name='guest'),
    path('guestdata', views.process_guest, name='guest-fun'),
]
