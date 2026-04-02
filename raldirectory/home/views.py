from django.shortcuts import render
from datetime import date

from aircraft.models import Aircraft


def home(request):
    target_day = date(2022, 2, 24)
    today = date.today()
    delta = -(target_day - today)

    last_updates = Aircraft.objects.prefetch_related('aircraftphoto_set').order_by('date')[:3]

    context = {
        'day_of_war': delta.days,
        'last_updates': last_updates
    }

    return render(request, "home/index.html", context)
