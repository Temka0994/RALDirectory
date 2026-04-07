from django.shortcuts import render

from aircraft.models import Aircraft
from django.db.models import F


def home(request):
    last_updates = Aircraft.objects.prefetch_related('aircraftphoto_set').order_by(F('date').desc(nulls_last=True))[:3]

    context = {
        'last_updates': last_updates
    }

    return render(request, "home/index.html", context)
