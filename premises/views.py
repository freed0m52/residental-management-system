from django.shortcuts import render

from db.database import get_connection


def premises(request):
    conn = get_connection()
    premises_list = conn.execute(
        "SELECT * FROM premises ORDER BY number"
    ).fetchall()
    conn.close()

    return render(
        request, "premises/premise_list.html", {"premises": premises_list}
    )


def premise_detail(request, premise_id: int):
    conn = get_connection()
    premise = conn.execute(
        "SELECT * FROM premises WHERE id = ?", [premise_id]
    ).fetchone()
    conn.close()

    if premise is None:
        return render(request, "404.html", status=404)

    return render(
        request, "premises/premise_detail.html", {"premise": premise}
    )
