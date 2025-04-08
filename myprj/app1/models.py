from django.db import models

class Patient(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100)
    age = models.IntegerField()
    department = models.CharField(max_length=100)
    dname = models.CharField(max_length=100)

class Doctor(models.Model):
    id=models.AutoField(primary_key=True)
    name=models.CharField(max_length=100)
    department = models.CharField(max_length=100)
    def __str__(self):
        return self.name
    
class Nurse(models.Model):
    id=models.AutoField(primary_key=True)
    name=models.CharField(max_length=100)
    department = models.CharField(max_length=100)
    def __str__(self):
        return self.name
# Create your models here.
