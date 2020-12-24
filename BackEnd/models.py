from django.db import models
from django.db.models.deletion import CASCADE
from django.contrib.auth.models import User as us

# Create your models here.


class Priosner(models.Model):
    NIC = models.CharField(max_length=13, primary_key=True)
    first_Name = models.CharField(max_length=30)
    last_Name = models.CharField(max_length=30)
