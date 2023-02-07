from django.contrib.auth import views as auth_views
from django.urls import include, path

from . import views

urlpatterns = [
    path('', include('django.contrib.auth.urls')),
    path('signup/', views.signup, name='signup'),
    path('signup/pacient/', views.PacientSignUpView.as_view(), name='pacient_signup'),
    path('signup/doctor/', views.DoctorSignUpView.as_view(), name='doctor_signup'),
    path('login/', views.login, name='login'),
]