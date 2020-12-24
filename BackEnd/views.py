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


def viewPrisoner(request):
    return render(request, 'BackEnd/viewPrisoner.html')


def transfer(request):
    return render(request, 'BackEnd/transfer.html')


def assets(request):
    return render(request, 'BackEnd/Assets.html')


def crimeDetails(request):
    return render(request, 'BackEnd/crimeDetails.html')


def sentence(request):
    return render(request, 'BackEnd/Sentence.html')


def personalInfo(request):
    return render(request, 'BackEnd/personalInfo.html')
