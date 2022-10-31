from django.urls import path
from django.contrib import admin
from . import views


urlpatterns = [
    path('', views.init, name="home"),
    path('topic/<int:pk>', views.topic, name="topic"),
    path('login', views.login, name="login"),
    path('lk', views.lk, name="lk"),
    path('exit', views.exit, name="exit")
]