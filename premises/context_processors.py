from .models import Premise


def premise_context(request):
    """Передаёт общие данные в шаблоны."""
    return {
        "site_name": "Жилой комплекс",
        "premises_count": Premise.objects.count(),
    }
