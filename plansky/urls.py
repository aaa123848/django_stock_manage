"""plansky URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url
from django.contrib import admin
from login import views as views_login
from polls import views as views_polls

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^index/', views_login.index),
    url(r'^login/', views_login.login),
    url(r'^logout/', views_login.logout),
    url(r'^stock/', views_polls.stock),
    url(r'^output/', views_polls.stockoutput),
    url(r'^import/', views_polls.stockimport),
    url(r'^stocksheet/',  views_polls.stocksheet),
    url(r'^base/', views_polls.base),
    url(r'^revise/', views_polls.revise)
]
