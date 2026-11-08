from django.shortcuts import render, get_object_or_404

from premises.models import Premise


def premises(request):
    premises_list = Premise.objects.all().order_by("number")
    return render(request, "premises/premise_list.html", {"premises": premises_list})


def premise_detail(request, slug):
    premise = get_object_or_404(Premise, slug=slug)
    return render(request, "premises/premise_detail.html", {"premise": premise})
