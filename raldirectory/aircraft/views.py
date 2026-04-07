from django.shortcuts import render, get_object_or_404
from aircraft.models import Aircraft


def aircraft_detail(request, pk):
    aircraft = get_object_or_404(Aircraft, pk=pk)
    return render(request, "aircraft/detail.html", {'aircraft': aircraft})
