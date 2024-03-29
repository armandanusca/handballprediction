"""mysite URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
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
from django.urls import path, include, re_path
from search.views import searchView
from home.views import homePage
from playerProfile.views import viewPlayer
from mlstats.views import mlStats

urlpatterns = [
    re_path(r'^$', homePage, name = 'home'),
    path('admin/', admin.site.urls),
    re_path(r'^search.*$', searchView, name = 'search'),
    re_path(r'^player.*$', viewPlayer, name = 'player'),
    re_path(r'^ml.*$', mlStats, name = 'mlstats')
]
