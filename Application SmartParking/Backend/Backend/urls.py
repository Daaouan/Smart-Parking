"""
URL configuration for Backend project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
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
from django.conf.urls import url
from BackendApp import views

from BackendApp.views import video_feed
from BackendApp.views import index


urlpatterns = [
    path('', index, name='index'),
   # path('parking', index, name='index'),

    url(r'^car$',views.carApi),
    url(r'^car/([0-9]+)$',views.carApi),

    url(r'^abonnement$',views.abonnementApi),
    url(r'^abonnement/([0-9]+)$',views.abonnementApi),

    url(r'^tableComplet$',views.tableCompletApi),
    url(r'^tableComplet/(?P<matricule>\w+)$',views.tableCompletApi),

    url(r'^entryTable$',views.entryTableApi),
    url(r'^entryTable/([0-9]+)$',views.entryTableApi),

    url(r'^outTable$',views.outTableApi),
    url(r'^outTable/([0-9]+)$',views.outTableApi),

    path('admin/', admin.site.urls),

    path('video_feed/', video_feed, name='video_feed'),

]