from cloudinary.models import CloudinaryField
from django.db import models


class Rank(models.Model):
    name = models.CharField(max_length=25, verbose_name="Звання")
    order = models.IntegerField(verbose_name="Цінність звання")


class Aircrew(models.Model):
    first_name = models.CharField(max_length=25, verbose_name="Ім'я")
    last_name = models.CharField(max_length=25, verbose_name="Прізвище")
    middle_name = models.CharField(max_length=25, null=True, blank=True, verbose_name="По-батькові")
    rank = models.ForeignKey(Rank, on_delete=models.SET_NULL, null=True, verbose_name="Звання")
    date_of_birth = models.DateField(null=True, blank=True, verbose_name="Дата народження")
    date_of_death = models.DateField(null=True, blank=True, verbose_name="Дата смерті")
    description = models.TextField(null=True, blank=True, verbose_name="Інформація")
    photo = CloudinaryField('image', null=True, blank=True)


class AircraftCrew(models.Model):
    aircraft = models.ForeignKey("aircraft.Aircraft", on_delete=models.CASCADE, verbose_name="Борт")
    aircrew_member = models.ForeignKey(Aircrew, on_delete=models.CASCADE, verbose_name="Член екіпажу")
