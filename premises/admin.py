from django.contrib import admin

from .models import Premise
from residents.models import Request


class RequestInline(admin.TabularInline):
    model = Request
    extra = 0
    fields = ("resident", "request_type", "status")


@admin.register(Premise)
class PremiseAdmin(admin.ModelAdmin):
    list_display = ("id", "number", "premise_type", "area", "is_large")
    list_filter = ("premise_type", "is_large")
    search_fields = ("number", "premise_type")
    readonly_fields = ("slug", "is_large")
    inlines = [RequestInline]
