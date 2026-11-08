from django.contrib import admin

from .models import Resident, Request


class RequestInline(admin.TabularInline):
    model = Request
    extra = 0
    fields = ("premise", "request_type", "status")


@admin.register(Resident)
class ResidentAdmin(admin.ModelAdmin):
    list_display = ("id", "full_name", "apartment_number", "status")
    list_display_links = ("full_name",)
    search_fields = ("full_name", "phone")
    list_filter = ("status",)
    inlines = [RequestInline]


@admin.register(Request)
class RequestAdmin(admin.ModelAdmin):
    list_display = ("id", "resident", "premise", "request_type", "status")
    list_filter = ("status", "request_type")
    search_fields = ("resident__full_name", "premise__number")
    list_select_related = ("resident", "premise")  # Оптимизация
