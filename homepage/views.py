from django.http import HttpResponse


BOOTSTRAP_CSS = (
    "https://cdn.jsdelivr.net/npm/bootstrap@5.3.0/dist/css/bootstrap.min.css"
)


def page(title, content):
    """Собрать HTML-страницу с общим каркасом."""
    return f"""<!DOCTYPE html>
<html lang="ru">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>{title}</title>
    <link href="{BOOTSTRAP_CSS}" rel="stylesheet">
</head>
<body>
    <nav class="navbar navbar-expand-lg navbar-dark bg-primary mb-4">
        <div class="container">
            <a class="navbar-brand" href="/">🏢 Жилой комплекс</a>
            <div class="navbar-nav">
                <a class="nav-link" href="/residents/">Жители</a>
                <a class="nav-link" href="/premises/">Помещения</a>
            </div>
        </div>
    </nav>
    <div class="container">
        {content}
    </div>
</body>
</html>"""


def index(request):
    """Главная страница."""
    content = """
    <h1 class="display-4">Система управления жилым комплексом</h1>
    <p class="lead">Учёт жителей, помещений и заявок на обслуживание.</p>
    <a href="/residents/" class="btn btn-primary me-2">Жители</a>
    <a href="/premises/" class="btn btn-secondary">Помещения</a>
    """
    return HttpResponse(page("Жилой комплекс", content))
def page_not_found(request, exception):
    """Собственная страница 404."""
    content = """
    <h1 class="text-danger">404 — страница не найдена</h1>
    <p>Проверьте адрес или вернитесь на главную.</p>
    <a href="/" class="btn btn-primary">На главную</a>
    """
    return HttpResponse(
        page("404 — страница не найдена", content),
        status=404,
    )
