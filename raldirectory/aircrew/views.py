from django.core.paginator import Paginator
from django.shortcuts import render

from .models import Aircrew


def aircrew_main(request):
    aircrew = Aircrew.objects.select_related('rank').order_by('id')

    paginator = Paginator(aircrew, 9)
    page_number = request.GET.get("page")
    page_obj = paginator.get_page(page_number)

    return render(request, "aircrew/main.html", {"page_obj": page_obj})
