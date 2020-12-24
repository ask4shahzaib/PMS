from django.db import models
from django.db.models.deletion import CASCADE
from django.contrib.auth.models import User as us

# Create your models here.


class Priosner(models.Model):
    NIC = models.CharField(max_length=13, primary_key=True)
    first_Name = models.CharField(max_length=30, null=False)
    last_Name = models.CharField(max_length=30, null=False)
    age = models.IntegerField(null=False)
    address = models.CharField(max_length=999, null=False)
    choice = [('Male', 'Male'), ('Female', 'Female')]
    Gender = models.CharField(
        choices=choice, max_length=30, default=None, null=False)
    emergency = models.CharField(max_length=10)
    Assets = models.CharField(max_length=999)
    Assets = models.CharField(max_length=999)
    choice2 = [('A', 'A'), ('B', 'B'), ('C', 'C'), ('D', 'D')]
    category = models.CharField(
        choices=choice2, max_length=30, default=None, null=False)
    choice3 = [('To be Executed', 'To be Executed'),
               ('To be Freed', 'To be Freed')]
    criminalType = models.CharField(
        choices=choice3, max_length=30, default=None, null=False)
    choice4 = [('None', 'None'), ('Hanging', 'Hanging'), ('Electrocution', 'Electrocution'),
               ('Firing', 'Firing'), ('Gas Chamber', 'Gas Chamber'), ('Lethal Injection', 'Lethal Injection')]
    executionType = models.CharField(
        choices=choice4, max_length=30, default=None, null=False)
    date = models.DateField()
