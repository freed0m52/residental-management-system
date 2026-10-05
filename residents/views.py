from django.http import HttpResponse

from homepage.views import page
from models.residents import find_resident_by_apartment
from storage import load_residents


def residents(request):
    """Список жителей."""
    residents_list = load_residents("data/residents.json")

    items = ""
    for r in residents_list:
        items += (
            f'<li class="list-group-item">'
            f'{r.full_name} (кв. {r.apartment_number}), {r.status}'
            f'</li>'
        )

    content = f"""
    <h1>Жители</h1>
    <ul class="list-group">{items}</ul>
    """
    return HttpResponse(page("Жители", content))


def resident_detail(request, resident_id):
    """Страница жителя."""
    residents_list = load_residents("data/residents.json")
    resident = None
    for r in residents_list:
        if r.id == resident_id:
            resident = r
            break

    if resident is None:
        content = """
        <h1 class="text-danger">Житель не найден</h1>
        <a href="/residents/" class="btn btn-outline-secondary">
            ← к списку жителей
        </a>
        """
        return HttpResponse(
            page("Житель не найден", content),
            status=404,
        )

    content = f"""
    <div class="card">
        <div class="card-body">
            <h5 class="card-title">{resident.full_name}</h5>
            <p class="card-text"><strong>Квартира:</strong>
                {resident.apartment_number}</p>
            <p class="card-text"><strong>Телефон:</strong>
                {resident.phone}</p>
            <p class="card-text"><strong>Статус:</strong>
                {resident.status}</p>
            <a href="/residents/" class="btn btn-outline-secondary">
                ← к списку жителей
            </a>
        </div>
    </div>
    """
    return HttpResponse(page(resident.full_name, content))
