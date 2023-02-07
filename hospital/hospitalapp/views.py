from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.db.models import Q

from .forms import AddExaminationForm, EditExaminationForm, AddHospitalizationForm, EditHospitalizationForm, AddDoseForm

from .models import Department, Hospitalization, Examination, Medicine, Dose
from accounts.models import Doctor, Pacient


@login_required
def index(request):
    if request.user.is_pacient:
        hospitalizations = Hospitalization.objects.filter(
            pacient__user=request.user)
        examinations = Examination.objects.filter(pacient__user=request.user)
        dosages = Dose.objects.filter(pacient__user=request.user)
        return render(request, 'hospitalapp/index_pacient.html', context={'hospitalizations': hospitalizations,
                                                                          'examinations': examinations,
                                                                          'doses': dosages})

    elif request.user.is_doctor:
        return render(request, 'hospitalapp/index_doctor.html', context={'user': request.user})

    return render(request, 'hospitalapp/index.html', context={})


@login_required
def search_result(request):
    if request.method == 'POST':
        searched = request.POST.get('searched')

        if request.user.is_pacient:
            if not searched:
                qs = Doctor.objects.all()
            else:
                qs = Doctor.objects.filter(Q(user__first_name__iexact=searched) | Q(
                    user__last_name__iexact=searched) | Q(user__username__iexact=searched))
            return render(request, 'hospitalapp/search_result_doctors.html', {'searched': searched, 'qs': qs, 'search_doctors': True})

        elif request.user.is_doctor:
            if not searched:
                qs = Doctor.objects.all()
            else:
                qs = Pacient.objects.filter(Q(user__first_name__iexact=searched) | Q(
                    user__last_name__iexact=searched) | Q(user__username__iexact=searched))
            return render(request, 'hospitalapp/search_result_pacients.html', {'searched': searched, 'qs': qs})

    else:
        return render(request, 'hospitalapp/search_result.html')


@login_required
def patients(request):
    patients = Pacient.objects.all()
    return render(request, 'hospitalapp/patients.html', context={'patients': patients})


def doctors(request):
    qs = Doctor.objects.all()
    return render(request, 'hospitalapp/search_result_doctors.html', context={'qs': qs})


@login_required
def patient_details(request, patient_id):
    patient = get_object_or_404(Pacient, pk=patient_id)

    hospitalizations = Hospitalization.objects.filter(pacient=patient)
    examinations = Examination.objects.filter(pacient=patient)
    dosages = Dose.objects.filter(pacient=patient)
    return render(request, 'hospitalapp/patient_details.html', context={'patient': patient,
                                                                        'hospitalizations': hospitalizations,
                                                                        'examinations': examinations,
                                                                        'dosages': dosages})


@login_required
def examinations(request):
    examinations = Examination.objects.all()
    return render(request, 'hospitalapp/records/examinations.html', context={'examinations': examinations})


@login_required
def add_examination(request):
    if request.method == 'POST':
        form = AddExaminationForm(request.POST)
        if form.is_valid():
            examination = form.save(commit=False)
            examination.doctor = request.user.doctor
            examination.pacient = form.cleaned_data['patient']
            examination.save()

            return redirect('/examinations')
    else:
        form = AddExaminationForm

    return render(request, 'hospitalapp/records/add_examination.html', {'form': form})


@login_required
def edit_examination(request, examination_id):
    e = get_object_or_404(Examination, pk=examination_id)
    if request.method == 'POST':
        form = EditExaminationForm(request.POST, instance=e)
        if form.is_valid():
            e = form.save(commit=False)
            e.save()
            return redirect('/examinations')
    else:
        form = EditExaminationForm(instance=e)

    return render(request, 'hospitalapp/records/edit_examination.html', {'examination': e, 'form': form})


@login_required
def delete_examination(request, examination_id):
    e = get_object_or_404(Examination, pk=examination_id)
    if request.method == 'POST':
        e.delete()
        return redirect('/examinations')

    return render(request, 'hospitalapp/records/delete_examination.html', {'examination': e})


@login_required
def hospitalizations(request):
    hospitalizations = Hospitalization.objects.all()
    return render(request, 'hospitalapp/records/hospitalizations.html', context={'hospitalizations': hospitalizations})


@login_required
def add_hospitalization(request):
    if request.method == 'POST':
        form = AddHospitalizationForm(request.POST)
        if form.is_valid():
            hospitalization = form.save(commit=False)
            hospitalization.doctor = request.user.doctor
            hospitalization.pacient = form.cleaned_data['patient']
            hospitalization.save()

            return redirect('/hospitalizations')
    else:
        form = AddHospitalizationForm

    return render(request, 'hospitalapp/records/add_hospitalization.html', {'form': form})


@login_required
def edit_hospitalization(request, hospitalization_id):
    h = get_object_or_404(Hospitalization, pk=hospitalization_id)
    if request.method == 'POST':
        form = EditHospitalizationForm(request.POST, instance=h)
        if form.is_valid():
            h = form.save(commit=False)
            h.save()
            return redirect('/hospitalizations')
    else:
        form = EditHospitalizationForm(instance=h)

    return render(request, 'hospitalapp/records/edit_hospitalization.html', {'hospitalization': h, 'form': form})


@login_required
def delete_hospitalization(request, hospitalization_id):
    h = get_object_or_404(Hospitalization, pk=hospitalization_id)
    if request.method == 'POST':
        h.delete()
        return redirect('/hospitalizations')

    return render(request, 'hospitalapp/records/delete_hospitalization.html', {'hospitalization': h})


@login_required
def dosages(request):
    dosages = Dose.objects.all()
    return render(request, 'hospitalapp/records/dosages.html', context={'dosages': dosages})


@login_required
def add_dosage(request):
    if request.method == 'POST':
        form = AddDoseForm(request.POST)
        if form.is_valid():
            dosage = form.save(commit=False)
            dosage.pacient = form.cleaned_data['patient']
            dosage.save()

            return redirect('/dosages')
    else:
        form = AddDoseForm

    return render(request, 'hospitalapp/records/add_dosage.html', {'form': form})


@login_required
def delete_dosage(request, dosage_id):
    dosage = get_object_or_404(Dose, pk=dosage_id)
    if request.method == 'POST':
        dosage.delete()
        return redirect('/dosages')

    return render(request, 'hospitalapp/records/delete_dosage.html', {'dosage': dosage})


@login_required
def medications(request):
    medications = Medicine.objects.all()
    return render(request, 'hospitalapp/records/medications.html', context={'medications': medications})
