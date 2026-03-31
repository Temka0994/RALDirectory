from django.db import models

from raldirectory.aircraft.models import Aircraft


class Rank(models.Model):
    name = models.CharField(max_length=25, verbose_name="Звання")
    order = models.IntegerField(verbose_name="Цінність звання")


class Aircrew(models.Model):
    first_name = models.CharField(max_length=25, verbose_name="Ім'я")
    last_name = models.CharField(max_length=25, verbose_name="Прізвище")
    middle_name = models.CharField(max_length=25, null=True, verbose_name="По-батькові")
    rank = models.ForeignKey(Rank, on_delete=models.SET_NULL, null=True, verbose_name="Звання")
    date_of_birth = models.DateField(null=True, verbose_name="Дата народження")
    date_of_death = models.DateField(null=True, verbose_name="Дата смерті")
    description = models.TextField(verbose_name="Інформація")
    photo_url = models.CharField(max_length=200, null=True, verbose_name="Посилання на фото")


class AircraftCrew(models.Model):
    aircraft = models.ForeignKey(Aircraft, on_delete=models.CASCADE, verbose_name="Борт")
    aircrew_member = models.ForeignKey(Aircrew, on_delete=models.CASCADE, verbose_name="Член екіпажу")
