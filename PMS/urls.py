from django.contrib import admin
from django.urls import path
from BackEnd import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.login),
    path('register/', views.register),
    path('view/', views.view),
    path('ohome/', views.ohome, name='ohome'),
    path('jhome/', views.jhome, name='jhome'),
]
