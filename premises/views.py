from django.shortcuts import render, get_object_or_404
from premises.models import Premise


def premises(request):
    # Получаем помещения через ORM
    premises_list = Premise.objects.all().order_by("number")
    return render(
        request, "premises/premise_list.html", {"premises": premises_list}
    )


def premise_detail(request, premise_id: int):
    premise = get_object_or_404(Premise, pk=premise_id)
    return render(
        request, "premises/premise_detail.html", {"premise": premise}
    )
