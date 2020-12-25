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
            "21/12/2008", "%d/%m/%Y").strftime("%Y-%m-%d")

        # cnic = '36402'
        # fname = 'Test'
        # lname = 'Prisoner'
        # age = 20
        # address = '852-B'
        # gender = 'Male'
        # emergency = '3212233444'
        # assets = 'Poor Nigga'
        # crime = '3 A*"s" on transcript'
        # category = 'To be Executed'
        # type = 'A'
        # execution = 'Firing'
        # date = '2020-10-10'

        x = Prisoner(NIC=cnic, first_Name=fname, last_Name=lname, age=age, address=address, Gender=gender,
                     emergency=emergency, Assets=assets, crimeDetails=crime, category=category,
                     criminalType=type, executionType=execution, date=date)
        x.save()
        # print('Saved Successfully')
    # return redirect('/')
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
