from django.db import models
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    is_pacient = models.BooleanField(default=False)
    is_doctor = models.BooleanField(default=False)
    def __str__(self):
        return self.username

class Pacient(models.Model):
    user = models.OneToOneField(
        'User', primary_key=True, on_delete=models.CASCADE)
    date_of_birth = models.DateField(blank=False, null=False)
    residence = models.CharField(blank=True, null=True, max_length=100)
    health_insurance = models.CharField(blank=True, null=True, max_length=100)

    def __str__(self):
        return self.user.username

class Doctor(models.Model):
    user = models.OneToOneField(
        'User', primary_key=True, on_delete=models.CASCADE)
    phone = models.CharField(blank=True, null=True, max_length=50)
    departments = models.ManyToManyField(
        'hospitalapp.Department', related_name='departments')

    def __str__(self):
        return self.user.username