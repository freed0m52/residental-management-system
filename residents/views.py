from django.shortcuts import render, get_object_or_404
from django.core.paginator import Paginator
from residents.models import Resident


def residents(request):
    # Получаем всех жителей через ORM, сортируем по ФИО
    residents_list = Resident.objects.all().order_by("full_name")

    # Пагинация: по 3 записи на страницу
    paginator = Paginator(residents_list, 3)
    page_obj = paginator.get_page(request.GET.get("page"))

    return render(
        request, "residents/resident_list.html", {"residents": page_obj, "page_obj": page_obj}
    )


def resident_detail(request, resident_id: int):
    # Ищем жителя по ID. Если нет - сразу отдаем 404
    resident = get_object_or_404(Resident, pk=resident_id)
    return render(request, "residents/resident_detail.html", {"resident": resident})
