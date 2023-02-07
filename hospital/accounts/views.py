from django.contrib.auth import authenticate, login
from django.shortcuts import redirect, render
from django.views.generic import CreateView

from .forms import PacientSignUpForm, DoctorSignUpForm
from .models import User, Pacient, Doctor


def signup(request):
    return render(request, 'accounts/signup.html', {})


class PacientSignUpView(CreateView):
    model = User
    form_class = PacientSignUpForm
    template_name = 'accounts/signup_pacient.html'

    def get_context_data(self, **kwargs):
        kwargs['user_type'] = 'pacient'
        return super().get_context_data(**kwargs)

    def form_valid(self, form):
        pacient = form.save()
        pacient = authenticate(username=form.cleaned_data['username'],
                               password=form.cleaned_data['password1'],
                               )
        login(self.request, pacient)
        return redirect('/')


class DoctorSignUpView(CreateView):
    model = User
    form_class = DoctorSignUpForm
    template_name = 'accounts/signup_doctor.html'

    def get_context_data(self, **kwargs):
        kwargs['user_type'] = 'doctor'
        return super().get_context_data(**kwargs)

    def form_valid(self, form):
        doctor = form.save()
        doctor = authenticate(username=form.cleaned_data['username'],
                              password=form.cleaned_data['password1'],
                              )
        login(self.request, doctor)
        return redirect('/')
