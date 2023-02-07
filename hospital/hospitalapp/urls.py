from django.urls import path, include 
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('search_result/', views.search_result, name='search_result'),
    path('patients/', views.patients, name='patients'),
    path('doctors/', views.doctors, name='doctors'),
    path('patient/<int:patient_id>/', views.patient_details, name='patient_details'),
    path('examinations/', views.examinations, name='examinations'),
    path('hospitalizations/', views.hospitalizations, name='hospitalizations'),
    path('dosages/', views.dosages, name='dosages'),
    path('hospitalizations/add/', views.add_hospitalization, name='add_hospitalization'),
    path('hospitalizations/<int:hospitalization_id>/edit/', views.edit_hospitalization, name='edit_hospitalization'),
    path('hospitalizations/<int:hospitalization_id>/delete/', views.delete_hospitalization, name='delete_hospitalization'),
    path('examinations/add/', views.add_examination, name='add_examination'),
    path('examinations/<int:examination_id>/edit/', views.edit_examination, name='edit_examination'),
    path('examinations/<int:examination_id>/delete/', views.delete_examination, name='delete_examination'),
    path('dosages/add/', views.add_dosage, name='add_dosage'),
    path('dosages/<int:dosage_id>/delete/', views.delete_dosage, name='delete_dosage'),
    path('dosages/medications/', views.medications, name='medications'),

]

