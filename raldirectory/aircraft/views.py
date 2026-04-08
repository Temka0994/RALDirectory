from django.core.paginator import Paginator
from django.shortcuts import render, get_object_or_404
from aircraft.models import Aircraft
from django.db.models import F


def aircraft_detail(request, pk):
    aircraft = get_object_or_404(Aircraft, pk=pk)
    return render(request, "aircraft/detail.html", {'aircraft': aircraft})


def aircraft_main(request):
    aircrafts = Aircraft.objects.prefetch_related('aircraftphoto_set').order_by(F('date').desc(nulls_last=True))

    paginator = Paginator(aircrafts, 5)
    page_number = request.GET.get("page")
    page_obj = paginator.get_page(page_number)

    return render(request, "aircraft/main.html", {"page_obj": page_obj})
