from django.db import models

class Patient(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100)
    age = models.IntegerField()

class Doctor(models.Model):
    id=models.AutoField(primary_key=True)
    name=models.CharField(max_length=100)
    dept=models.CharField(max_length=100)
# Create your models here.
