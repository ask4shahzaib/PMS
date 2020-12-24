from django.contrib import admin
from django.urls import path
from BackEnd import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('register/', views.register, name='register'),
    path('assets/', views.assets, name='assets'),
    path('crimeDetails/', views.crimeDetails, name='crimeDetails'),
    path('', views.login, name='home'),
    path('jhome/', views.jhome, name='jhome'),
    path('ohome/', views.ohome, name='ohome'),
    path('personalInfo/', views.personalInfo, name='personalInfo'),
    path('sentence/', views.sentence, name='sentence'),
    path('transfer/', views.transfer, name='transfer'),
    path('viewPrisoner/', views.viewPrisoner, name='viewPrisoner'),
]
