from django.shortcuts import render,redirect,get_object_or_404
from django.http import HttpResponse
from django.http import JsonResponse
from django.contrib import messages
from rest_framework import generics
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import status
from .serializers import *
from .models import *

def home(request):
    patient = Patient.objects.all()
    department = Doctor.objects.values_list('department', flat=True).distinct()  # Get unique departments
    context = {'ses':request.session.get('name_s'),
               'patient': patient ,'department': department}
    return render(request, 'home.html', context)

def go_to_react_doctor(request):
    return redirect("http://localhost:5173/doctordet")

def reg_new_doctor(request):
    return redirect('http://localhost:5173/doctor')

def reg_new_nurse(request):
    return redirect('http://localhost:5173/nurse')

def get_doctors(request):
    department = request.GET.get('department')  # Get department from request
    if department:  # Ensure department is provided
        doctors = Doctor.objects.filter(department=department).values_list('name', flat=True)
        return JsonResponse({'doctors': list(doctors)})
    return JsonResponse({'doctors': []})  # Return empty list if department is not found
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
        department=request.POST['department']
        data=Patient(name=name,age=age,department=department)
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

@api_view(['POST'])
def create_doctor(request):
    if request.method == 'POST':
        serializer = Doctor_szr(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['POST'])
def create_nurse(request):
    if request.method == 'POST':
        serializer = Nurse_szr(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
class doctorget(generics.ListAPIView):
    queryset = Doctor.objects.all()
    serializer_class = Doctor_szr

class nurseget(generics.ListAPIView):
    queryset = Nurse.objects.all()
    serializer_class = Nurse_szr
class putdoctorget(generics.RetrieveUpdateDestroyAPIView):
    queryset = Doctor.objects.all()
    serializer_class = Doctor_szr
    lookup_field = 'name'
class putnurseget(generics.RetrieveUpdateDestroyAPIView):
    queryset = Nurse.objects.all()
    serializer_class = Nurse_szr
    lookup_field = 'name'
class DoctorCreateView(generics.CreateAPIView):
    queryset = Doctor.objects.all()
    serializer_class = Doctor_szr
class NurseCreateView(generics.CreateAPIView):
    queryset = Nurse.objects.all()
    serializer_class = Nurse_szr
    
def add_doctor(request):
    if request.method == 'GET':
        doctor = Doctor.objects.all()

def add_nurse(request):
    if request.method == 'GET':
        nurse = Nurse.objects.all()
        
# Create your views here.
