from django.urls import path,include
from .import views
from .views import DoctorCreateView 
urlpatterns = [
    path('', views.login, name='login'),
    path('patientsession/', views.patientsession, name='patientsession'),
    path('logout/', views.logout, name='logout'),
    path('home/', views.home, name='home'),
    path('patientupd/', views.patientupd, name='patientupd'),
    path('patientdet/', views.patientdet, name='patientdet'),
    path('add_patient/', views.add_patient, name='add_patient'),
    path('upd_patient/<int:id>/', views.upd_patient, name='upd_patient'),
    path('del_patient/<int:id>/', views.del_patient, name='del_patient'),
    path('patientget/', views.patientget.as_view(), name='patientget'),
    path('putpatientget/', views.putpatientget.as_view(), name='putpatientget'),
    path('doctorcreate/', DoctorCreateView.as_view(), name='doctorcreate'),
    path('nursecreate/', views.NurseCreateView.as_view(), name='nursecreate'),
    path('doctorget/', views.doctorget.as_view(), name='doctorget'),
    path('nurseget/', views.nurseget.as_view(), name='nurseget'),
    path('putdoctorget/', views.putdoctorget.as_view(), name='putdoctorget'),
    path('putnurseget/', views.putnurseget.as_view(), name='putnurseget'),
    path('get_doctors/', views.get_doctors, name='get_doctors'),
    path('go-to-doctor/', views.go_to_react_doctor, name='go_to_doctor'),
    path('reg_new_doctor/', views.reg_new_doctor, name='reg_new_doctor'),
    path('reg_new_nurse/', views.reg_new_nurse, name='reg_new_nurse'),
]
