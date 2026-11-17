from django.shortcuts import render, get_object_or_404, redirect
from django.db.models import Q
from premises.models import Premise
from residents.forms import PremiseForm


def premises(request):
    """Список помещений с фильтрацией и сортировкой."""
    premises_list = Premise.objects.all()

    # по номеру
    search_query = request.GET.get("q", "").strip()
    if search_query:
        premises_list = premises_list.filter(number__icontains=search_query)

    # по типу
    type_filter = request.GET.get("type", "")
    if type_filter:
        premises_list = premises_list.filter(premise_type=type_filter)

    # сортировка
    sort = request.GET.get("sort", "number")
    if sort in ["number", "-number", "area", "-area"]:
        premises_list = premises_list.order_by(sort)

    raw_types = Premise.objects.values_list("premise_type", flat=True)
    cleaned_types = [t.strip().capitalize() for t in raw_types if t]
    
    types = sorted(list(set(cleaned_types)))

    return render(request, "premises/premise_list.html", {
        "premises": premises_list,
        "search_query": search_query,
        "type_filter": type_filter,
        "sort": sort,
        "types": types,
    })


def premise_detail(request, slug):
    premise = get_object_or_404(Premise, slug=slug)
    return render(request, "premises/premise_detail.html", {"premise": premise})


def premise_create(request):
    if request.method == "POST":
        form = PremiseForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("premises:list")
    else:
        form = PremiseForm()
    return render(request, "premises/premise_form.html", {"form": form})
