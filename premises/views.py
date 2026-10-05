from django.http import HttpResponse

from homepage.views import page
from storage import load_premises


def premises(request):
    """Список помещений."""
    premises_list = load_premises("data/premises.json")

    items = ""
    for p in premises_list:
        items += (
            f'<li class="list-group-item">'
            f'{p}'
            f'</li>'
        )

    content = f"""
    <h1>Помещения</h1>
    <ul class="list-group">{items}</ul>
    """
    return HttpResponse(page("Помещения", content))


def premise_detail(request, premise_id):
    """Страница помещения."""
    premises_list = load_premises("data/premises.json")
    premise = None
    for p in premises_list:
        if p.id == premise_id:
            premise = p
            break

    if premise is None:
        content = """
        <h1 class="text-danger">Помещение не найдено</h1>
        <a href="/premises/" class="btn btn-outline-secondary">
            ← к списку помещений
        </a>
        """
        return HttpResponse(
            page("Помещение не найдено", content),
            status=404,
        )

    content = f"""
    <div class="card">
        <div class="card-body">
            <h5 class="card-title">Помещение №{premise.number}</h5>
            <p class="card-text"><strong>Тип:</strong>
                {premise.premise_type}</p>
            <p class="card-text"><strong>Площадь:</strong>
                {premise.area} кв.м.</p>
            <a href="/premises/" class="btn btn-outline-secondary">
                ← к списку помещений
            </a>
        </div>
    </div>
    """
    return HttpResponse(page(f"Помещение №{premise.number}", content))
