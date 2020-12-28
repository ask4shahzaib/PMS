from django.http.response import HttpResponse
from django.shortcuts import redirect, render
from .forms import *
import datetime
from .models import *

# Create your views here.


def login(request):
    return render(request, 'BackEnd/index.html')


def ohome(request):
    return render(request, 'BackEnd/officer.html')


def jhome(request):
    return render(request, 'BackEnd/jailor.html')


def register(request):
    if request.method == 'POST':
        cnic = request.POST['NIC']
        fname = request.POST['fname']
        lname = request.POST['lname']
        age = request.POST['age']
        age = int(age)
        address = request.POST['address']
        gender = request.POST['gender']
        emergency = request.POST['phone']
        assets = request.POST['assets']
        crime = request.POST['crime']
        category = request.POST['category']
        type = request.POST['type']
        execution = request.POST['execution']
        date = request.POST['date']
        date = datetime.datetime.strptime(
            date, '%Y-%m-%d').strftime("%Y-%m-%d")

        x = Prisoner(NIC=cnic, first_Name=fname, last_Name=lname, age=age, address=address, Gender=gender,
                     emergency=emergency, Assets=assets, crimeDetails=crime, category=category,
                     criminalType=type, executionType=execution, date=date)
        x.save()
    return render(request, 'BackEnd/register.html')


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
