from django.db import models


class AircraftType(models.TextChoices):
    HELICOPTER = "HELICOPTER", "Helicopter"
    PLANE = "PLANE", "Plane"


class TailColor(models.TextChoices):
    BLUE = "BLUE", "Blue"
    RED = "RED", "Red"
    WHITE = "WHITE", "White"
    YELLOW = "YELLOW", "Yellow"


class AircraftStatus(models.TextChoices):
    DAMAGED = "DAMAGED", "Damaged"
    DESTROYED = "DESTROYED", "Destroyed"
    CAPTURED = "CAPTURED", "Captured"


class Subdivision(models.Model):
    name = models.CharField(max_length=200, verbose_name="Назва підрозділу")
    military_unit_number = models.PositiveIntegerField(verbose_name="Номер військової частини")
    dislocation = models.CharField(max_length=200, verbose_name="Місце дислокації")


class AircraftModel(models.Model):
    name = models.CharField(max_length=25, verbose_name="Модель")


class Aircraft(models.Model):
    type = models.CharField(max_length=15, choices=AircraftType.choices, verbose_name="Тип")
    model = models.ForeignKey(AircraftModel, on_delete=models.SET_NULL, null=True, verbose_name="Модель")
    tail_number = models.PositiveIntegerField(null=True, blank=True, verbose_name="Бортовий номер")
    tail_color = models.CharField(max_length=10, choices=TailColor.choices, null=True, blank=True,
                                  verbose_name="Колір бортового номеру")
    register_number = models.CharField(max_length=10, null=True, blank=True, verbose_name="Реєстрційний номер")
    serial_number = models.PositiveIntegerField(null=True, blank=True, verbose_name="Серійний номер")
    subdivision = models.ForeignKey(Subdivision, on_delete=models.SET_NULL, null=True, verbose_name="Підрозділ")
    status = models.CharField(max_length=15, choices=AircraftStatus.choices, verbose_name="Статус")
    date = models.DateField(null=True, blank=True, verbose_name="Дата")
    location = models.CharField(max_length=200, null=True, blank=True, verbose_name="Локація")
    description = models.TextField(null=True, blank=True, verbose_name="Опис")


class AircraftPhoto(models.Model):
    aircraft = models.ForeignKey(Aircraft, on_delete=models.CASCADE)
    url = models.CharField(max_length=200, verbose_name="URL посилання")
