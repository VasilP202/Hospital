from secrets import choice
from django import forms
import datetime

from .models import Department, Examination, Hospitalization, Dose, Medicine
from accounts.models import Pacient
from hospital.constants import APPLICATION_METHOD_CHOICES


class AddExaminationForm(forms.ModelForm):

    class Meta:
        model = Examination
        fields = ('result', 'date', 'patient', 'department')

    date = forms.DateField(required=True, initial=datetime.date.today, input_formats=[
                           '%d-%m-%Y', '%Y-%m-%d', '%d.%m.%Y', '%Y.%m.%d'], )
    result = forms.CharField(required=True, widget=forms.Textarea(
        attrs={'name': 'body', 'rows': '3', 'cols': '50'}))

    patient = forms.ModelChoiceField(
        required=True, queryset=Pacient.objects.all(),
    )
    department = forms.ModelChoiceField(
        queryset=Department.objects.all(),
    )


class EditExaminationForm(forms.ModelForm):

    class Meta:
        model = Examination
        fields = ('result', 'date', 'department')

    date = forms.DateField(required=True, initial=datetime.date.today, input_formats=[
        '%d-%m-%Y', '%Y-%m-%d', '%d.%m.%Y', '%Y.%m.%d'], )
    result = forms.CharField(required=True, widget=forms.Textarea(
        attrs={'name': 'body', 'rows': '3', 'cols': '50'}))

    department = forms.ModelChoiceField(
        queryset=Department.objects.all(),
    )


class AddHospitalizationForm(forms.ModelForm):

    class Meta:
        model = Hospitalization
        fields = ('purpose', 'date', 'patient')

    date = forms.DateField(required=True, initial=datetime.date.today, input_formats=[
                           '%d-%m-%Y', '%Y-%m-%d', '%d.%m.%Y', '%Y.%m.%d'], )
    purpose = forms.CharField(label='Reason', required=True, widget=forms.Textarea(
        attrs={'name': 'body', 'rows': '3', 'cols': '50'}))

    patient = forms.ModelChoiceField(
        required=True, queryset=Pacient.objects.all(),
    )


class EditHospitalizationForm(forms.ModelForm):

    class Meta:
        model = Hospitalization
        fields = ('purpose', 'date')

    date = forms.DateField(required=True, initial=datetime.date.today, input_formats=[
                           '%d-%m-%Y', '%Y-%m-%d', '%d.%m.%Y', '%Y.%m.%d'], )
    purpose = forms.CharField(label='Reason', required=True, widget=forms.Textarea(
        attrs={'name': 'body', 'rows': '3', 'cols': '50'}))


class AddDoseForm(forms.ModelForm):

    class Meta:
        model = Dose
        fields = ('date', 'patient', 'medicine', 'application_method')

    date = forms.DateField(required=True, initial=datetime.date.today, input_formats=[
                           '%d-%m-%Y', '%Y-%m-%d', '%d.%m.%Y', '%Y.%m.%d'], )

    medicine = forms.ModelChoiceField(
        required=True, queryset=Medicine.objects.all())

    patient = forms.ModelChoiceField(
        required=True, queryset=Pacient.objects.all(),
    )

