from django.shortcuts import render, get_object_or_404, redirect
from django.core.paginator import Paginator
from django.db.models import Count, Q
from residents.models import Resident, Request
from premises.models import Premise
from .forms import RequestForm, PremiseForm, ResidentForm


def residents(request):
    """Список жителей с сортировкой."""
    residents_list = Resident.objects.all()
    
    # Сортировка
    sort = request.GET.get("sort", "full_name")
    if sort in ["full_name", "-full_name", "apartment_number"]:
        residents_list = residents_list.order_by(sort)

    # Пагинация
    paginator = Paginator(residents_list, 3)
    page_obj = paginator.get_page(request.GET.get("page"))

    return render(request, "residents/resident_list.html", {
        "residents": page_obj, 
        "page_obj": page_obj,
        "sort": sort
    })


def resident_detail(request, resident_id: int):
    resident = get_object_or_404(Resident, pk=resident_id)
    return render(request, "residents/resident_detail.html", {"resident": resident})

def resident_create(request):
    if request.method == "POST":
        form = ResidentForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("residents:list")
    else:
        form = ResidentForm()
    return render(request, "residents/resident_form.html", {"form": form})



def request_list(request):
    requests_list = Request.objects.all().select_related('resident', 'premise')
    
    # фильтрация по статусу
    status_filter = request.GET.get('status', '')
    if status_filter:
        requests_list = requests_list.filter(status=status_filter)
        
    # сортировка
    sort = request.GET.get('sort', '-created_at') # по умолчанию новые сверху
    if sort in ['created_at', '-created_at', 'request_type']:
        requests_list = requests_list.order_by(sort)

    # пагинация
    paginator = Paginator(requests_list, 5)
    page_obj = paginator.get_page(request.GET.get('page'))

    context = {
        'requests': page_obj,
        'page_obj': page_obj,
        'status_filter': status_filter,
        'sort': sort,
        'statuses': Request.Status.choices,
    }
    return render(request, 'residents/request_list.html', context)

def statistics(request):
    total_requests = Request.objects.count()
    new_requests = Request.objects.filter(status=Request.Status.NEW).count()
    in_progress = Request.objects.filter(status=Request.Status.IN_PROGRESS).count()
    completed = Request.objects.filter(status=Request.Status.COMPLETED).count()
    
    premise_stats = Premise.objects.annotate(req_count=Count('requests')).order_by('-req_count')

    context = {
        'total_requests': total_requests,
        'new_requests': new_requests,
        'in_progress': in_progress,
        'completed': completed,
        'premise_stats': premise_stats,
    }
    return render(request, 'residents/statistics.html', context)

def request_create(request):
    if request.method == 'POST':
        form = RequestForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('residents:requests')
    else:
        form = RequestForm()
    return render(request, 'residents/request_form.html', {'form': form})


