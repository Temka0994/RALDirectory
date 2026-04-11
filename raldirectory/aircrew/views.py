from django.core.paginator import Paginator
from django.db.models import Q
from django.shortcuts import render, get_object_or_404

from .models import Aircrew, Rank


def aircrew_main(request):
    aircrew = Aircrew.objects.select_related('rank')

    query = request.GET.get('q', '')
    rank = request.GET.get('rank', '')

    if query:
        aircrew = aircrew.filter(
            Q(last_name__icontains=query) |
            Q(first_name__icontains=query) |
            Q(middle_name__icontains=query)
        )
    if rank:
        aircrew = aircrew.filter(rank_id=rank)

    aircrew = aircrew.order_by('last_name')

    paginator = Paginator(aircrew, 9)
    page_obj = paginator.get_page(request.GET.get('page'))

    return render(request, "aircrew/main.html", {
        "page_obj": page_obj,
        "ranks": Rank.objects.order_by('order'),
        "q": query,
        "selected_rank": rank,
    })


def aircrew_detail(request, pk):
    aircrew = get_object_or_404(Aircrew, pk=pk)
    return render(request, "aircrew/detail.html", {'aircrew': aircrew})
