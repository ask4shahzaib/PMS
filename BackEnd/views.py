from django.http.response import HttpResponse
from django.shortcuts import render

# Create your views here.


def login(request):
    return render(request, 'BackEnd/index.html')


def ohome(request):
    return render(request, 'BackEnd/officer.html')


def jhome(request):
    return render(request, 'BackEnd/jailor.html')


def register(request):
    return render(request, 'BackEnd/addPrisoner.html')


def view(request):
    return render(request, 'BackEnd/personalInfo.html')
