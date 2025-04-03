from django.shortcuts import render,redirect,get_object_or_404
from django.http import HttpResponse
from django.contrib import messages
from rest_framework import generics
from .serializers import *
from .models import *

def home(request):
    patient = Patient.objects.all()
    context = {'ses':request.session.get('name_s'),
               'patient': patient}
    return render(request, 'home.html', context)

class patientget(generics.ListAPIView):
    queryset = Patient.objects.all()
    serializer_class = Patient_szr

class putpatientget(generics.RetrieveUpdateDestroyAPIView):
    queryset = Patient.objects.all()
    serializer_class = Patient_szr
    lookup_field = 'name'
    
def patientupd(request):
    return render(request, 'patientupd.html')

def login(request):
    return render(request, 'login.html')

def patientsession(request):
    if request.method == 'POST':
        name = request.POST['name']
        age = request.POST['age']
        if Patient.objects.filter(name=name,age=age).exists():
            data=Patient.objects.filter(name=name,age=age).values('name','age').first()
            request.session['name_s'] = data['name']
            request.session['age_s'] = data['age']
            return redirect('home')
        else:
            return render(request, 'login.html', {'msg':'Invalid Credentials'})
    else:
        return redirect('login')
    
def logout(request):
    request.session.flush()
    return redirect('login')

def patientdet(request):
    patients = Patient.objects.all()
    return render(request, 'patientdet.html', {'patients': patients})

def add_patient(request):
    if request.method == 'POST':
        name=request.POST['name']
        age=request.POST['age']
        data=Patient(name=name,age=age)
        data.save()
        messages.success(request, 'Patient added successfully')
        return redirect('patientdet')
    return render(request, 'home.html')

def upd_patient(request, id):
    patient = get_object_or_404(Patient, id=id)
    if request.method == 'POST':
        name=request.POST.get('name')
        age=request.POST.get('age')
        if name:
            patient.name = name
        if age:
            patient.age = age
        patient.save()
        messages.success(request, 'Patient updated successfully')
        return redirect('patientdet')
    return render(request, 'patientupd.html', {'patient': patient})

def del_patient(request, id):
    patient = Patient.objects.filter(id=id)
    patient.delete()
    messages.success(request, 'Patient deleted successfully')
    return redirect('home')
# Create your views here.
