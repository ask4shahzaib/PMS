from django.db import models
from django.db.models.deletion import CASCADE
from django.contrib.auth.models import User as us

# Create your models here.


class Prisoner(models.Model):
    NIC = models.CharField(max_length=13, primary_key=True)
    first_Name = models.CharField(max_length=30, null=False)
    last_Name = models.CharField(max_length=30, null=False)
    age = models.IntegerField(null=False)
    address = models.CharField(max_length=999, null=False)
    Gender = models.CharField(max_length=30, default=None, null=False)
    emergency = models.CharField(max_length=10)
    Assets = models.CharField(max_length=999)
    crimeDetails = models.CharField(max_length=999)
    category = models.CharField(max_length=30, default=None, null=False)
    criminalType = models.CharField(max_length=30, default=None, null=False)
    executionType = models.CharField(max_length=30, default=None, null=False)
    date = models.DateField()
