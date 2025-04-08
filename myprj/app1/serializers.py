from rest_framework import serializers
from .models import *

class Patient_szr(serializers.ModelSerializer):
    class Meta:
        model = Patient
        fields = '__all__'
        
class Doctor_szr(serializers.ModelSerializer):
    class Meta:
        model = Doctor
        fields = '__all__'
    
class Nurse_szr(serializers.ModelSerializer):
    class Meta:
        model = Nurse
        fields = '__all__'