from django.shortcuts import render

from db.database import get_connection


def residents(request):
    conn = get_connection()
    residents_list = conn.execute(
        "SELECT * FROM residents ORDER BY full_name"
    ).fetchall()
    conn.close()

    return render(
        request, "residents/resident_list.html", {"residents": residents_list}
    )


def resident_detail(request, resident_id: int):
    conn = get_connection()
    resident = conn.execute(
        "SELECT * FROM residents WHERE id = ?", [resident_id]
    ).fetchone()
    conn.close()

    if resident is None:
        return render(request, "404.html", status=404)

    return render(
        request, "residents/resident_detail.html", {"resident": resident}
    )
