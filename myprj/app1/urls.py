from django.urls import path,include
from .import views
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
]
