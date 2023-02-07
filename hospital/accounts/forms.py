from distutils.command.clean import clean
from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.db import transaction

from hospitalapp.models import Department
from .models import User, Pacient, Doctor


class PacientSignUpForm(UserCreationForm):

    date_of_birth = forms.DateField(required=True, input_formats=['%d-%m-%Y', '%Y-%m-%d', '%d.%m.%Y', '%Y.%m.%d'],
                                    widget=forms.DateInput(attrs={'placeholder': 'dd.mm.yyyy'}))
    residence = forms.CharField( required=True, max_length=200,
        widget=forms.TextInput(attrs={'placeholder': 'Brno'}))
    health_insurance = forms.CharField(required=False, max_length=200, 
        widget=forms.TextInput(attrs={'placeholder': 'VZP'}))

    first_name = forms.CharField(required=True, max_length=150, 
        widget=forms.TextInput(attrs={'placeholder': 'Jan'}))
    last_name = forms.CharField(required=True, max_length=150, 
        widget=forms.TextInput(attrs={'placeholder': 'Novák'}))

    class Meta(UserCreationForm.Meta):
        model = User
        fields = UserCreationForm.Meta.fields + ('first_name', 'last_name', 'username')

    def __init__(self, *args, **kwargs):
        super(UserCreationForm, self).__init__(*args, **kwargs)

        for fieldname in ['username', 'password1', 'password2']:
            self.fields[fieldname].help_text = None

    username = forms.EmailField(label='Email(username)', widget=forms.TextInput(
        attrs={'placeholder': 'novak@gmail.com'}))

    @transaction.atomic
    def save(self):
        user = super().save(commit=False)
        user.is_pacient = True
        user.email = user.username
        user.save()

        pacient = Pacient.objects.create(
            user=user, date_of_birth=self.cleaned_data['date_of_birth'],
            residence=self.cleaned_data['residence'],
            health_insurance=self.cleaned_data['health_insurance']
        )

        return pacient


class DoctorSignUpForm(UserCreationForm):

    phone = forms.CharField(required=False, widget=forms.TextInput(
        attrs={'placeholder': '+420773100100'}))

    departments = forms.ModelMultipleChoiceField(
        label='Departments (ICPE)',
        queryset=Department.objects.all(),
        widget=forms.CheckboxSelectMultiple,
        required=True
    )

    first_name = forms.CharField(required=True, max_length=150, 
        widget=forms.TextInput(attrs={'placeholder': 'Jan'}))
    last_name = forms.CharField(required=True, max_length=150, 
        widget=forms.TextInput(attrs={'placeholder': 'Novák'}))

    class Meta(UserCreationForm.Meta):
        model = User
        fields = UserCreationForm.Meta.fields + ('first_name', 'last_name', 'username')

    def __init__(self, *args, **kwargs):
        super(UserCreationForm, self).__init__(*args, **kwargs)

        for fieldname in ['username', 'password1', 'password2']:
            self.fields[fieldname].help_text = None

    username = forms.EmailField(label='Email(username)', widget=forms.TextInput(
        attrs={'placeholder': 'doctor@gmail.com'}))

    @transaction.atomic
    def save(self):
        user = super().save(commit=False)
        user.is_doctor = True
        user.save()

        doctor = Doctor.objects.create(
            user=user, phone=self.cleaned_data['phone'])
        doctor.departments.add(*self.cleaned_data.get('departments'))

        return doctor
