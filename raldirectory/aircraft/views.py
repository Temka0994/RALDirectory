from django.core.paginator import Paginator
from django.shortcuts import render, get_object_or_404
from aircraft.models import Aircraft, AircraftType, AircraftStatus
from django.db.models import F, Q


def aircraft_detail(request, pk):
    aircraft = get_object_or_404(Aircraft, pk=pk)
    return render(request, "aircraft/detail.html", {'aircraft': aircraft})


def aircraft_main(request):
    aircrafts = Aircraft.objects.prefetch_related('aircraftphoto_set').select_related('type', 'model', 'subdivision')

    query = request.GET.get('q', '')
    status = request.GET.get('status', '')
    aircraft_type = request.GET.get('type', '')

    if query:
        aircrafts = aircrafts.filter(
            Q(model__name__icontains=query) |
            Q(tail_number__icontains=query) |
            Q(register_number__icontains=query) |
            Q(serial_number__icontains=query) |
            Q(location__icontains=query)
        )
    if status:
        aircrafts = aircrafts.filter(status=status)
    if aircraft_type:
        aircrafts = aircrafts.filter(type_id=aircraft_type)

    aircrafts = aircrafts.order_by(F('date').desc(nulls_last=True))

    paginator = Paginator(aircrafts, 5)
    page_obj = paginator.get_page(request.GET.get('page'))

    return render(request, "aircraft/main.html", {
        "page_obj": page_obj,
        "aircraft_types": AircraftType.objects.all(),
        "aircraft_statuses": AircraftStatus.choices,
        "q": query,
        "selected_status": status,
        "selected_type": aircraft_type,
    })