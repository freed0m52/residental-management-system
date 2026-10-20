from django.shortcuts import render
from storage import load_premises

def premises(request):
    premises_list = load_premises("data/premises.json")
    context = {"premises": premises_list}
    return render(request, "premises/premise_list.html", context)

def premise_detail(request, premise_id: int):
    premises_list = load_premises("data/premises.json")
    premise = next((p for p in premises_list if p.id == premise_id), None)
    
    if premise is None:
        return render(request, "404.html", status=404)
        
    context = {"premise": premise}
    return render(request, "premises/premise_detail.html", context)
