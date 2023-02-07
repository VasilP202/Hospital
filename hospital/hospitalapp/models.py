from django.db import models
from datetime import datetime
from hospital.constants import APPLICATION_METHOD_CHOICES, APPLICATION_METHOD_ORALLY


class Department(models.Model):
    icpe = models.CharField(primary_key=True, max_length=8)
    title = models.CharField(null=False, max_length=100)

    def __str__(self):
        return self.title + '(%s)' % self.icpe


class Hospitalization(models.Model):
    purpose = models.CharField(blank=True, null=True, max_length=400)
    date = models.DateField(blank=False, null=False)
    pacient = models.ForeignKey('accounts.Pacient', on_delete=models.CASCADE)
    doctor = models.ForeignKey('accounts.Doctor', on_delete=models.CASCADE)

    class Meta:
        ordering = ['-date']


class Examination(models.Model):
    date = models.DateField(blank=False, null=False)
    result = models.CharField(blank=True, null=True, max_length=400)
    pacient = models.ForeignKey('accounts.Pacient', on_delete=models.CASCADE)
    doctor = models.ForeignKey('accounts.Doctor', on_delete=models.CASCADE)
    department = models.ForeignKey('Department', on_delete=models.CASCADE)

    class Meta:
        ordering = ['-date']


class Medicine(models.Model):
    title = models.CharField(unique=True, null=False,
                             blank=False, max_length=100)
    active_substance = models.CharField(null=True, blank=True, max_length=100)
    medicine_strenght = models.SmallIntegerField(
        verbose_name='Strength(mg)', null=True, blank=True)
    contraindications = models.CharField(null=True, blank=True, max_length=100)

    def __str__(self):
        return self.title


class Dose(models.Model):
    date = models.DateField(default=datetime.now, blank=True, null=True)
    medicine = models.ForeignKey('Medicine', on_delete=models.CASCADE)
    pacient = models.ForeignKey('accounts.Pacient', on_delete=models.CASCADE)
    application_method = models.SmallIntegerField(
        choices=APPLICATION_METHOD_CHOICES, default=APPLICATION_METHOD_ORALLY, null=False, blank=False)

    class Meta:
        ordering = ['-date']