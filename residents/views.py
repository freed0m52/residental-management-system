from django.shortcuts import render
from storage import load_residents

def residents(request):
    residents_list = load_residents("data/residents.json")
    context = {"residents": residents_list}
    return render(request, "residents/resident_list.html", context)

def resident_detail(request, resident_id: int):
    residents_list = load_residents("data/residents.json")
    resident = next((r for r in residents_list if r.id == resident_id), None)
    
    if resident is None:
        # Вместо raise Http404 рендерим красивую страницу с кодом 404
        return render(request, "404.html", status=404)
        
    context = {"resident": resident}
    return render(request, "residents/resident_detail.html", context)
