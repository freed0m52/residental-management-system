from django.db import models
from premises.models import Premise


class Resident(models.Model):
    """Модель жителя."""
    full_name = models.CharField(max_length=200, verbose_name="ФИО")
    apartment_number = models.PositiveIntegerField(verbose_name="Квартира")
    phone = models.CharField(
        max_length=20,
        verbose_name="Телефон",
        blank=True,
        null=True
    )
    status = models.CharField(max_length=50, verbose_name="Статус")

    class Meta:
        ordering = ["full_name"]
        verbose_name = "Житель"
        verbose_name_plural = "Жители"

    def __str__(self):
        return f"{self.full_name} (кв. {self.apartment_number})"


class Request(models.Model):
    """Модель заявки (связывает жителя и помещение)."""

    class Status(models.TextChoices):
        NEW = "new", "Новая"
        IN_PROGRESS = "in_progress", "В работе"
        COMPLETED = "completed", "Выполнена"

    resident = models.ForeignKey(
        Resident,
        on_delete=models.CASCADE,
        related_name="requests",
        verbose_name="Житель"
    )
    premise = models.ForeignKey(
        Premise,
        on_delete=models.CASCADE,
        related_name="requests",
        verbose_name="Помещение"
    )
    request_type = models.CharField(max_length=100, verbose_name="Тип заявки")
    description = models.TextField(verbose_name="Описание", blank=True)
    status = models.CharField(
        max_length=20,
        choices=Status.choices,
        default=Status.NEW,
        verbose_name="Статус"
    )
    created_at = models.DateTimeField(
        auto_now_add=True,
        verbose_name="Дата создания"
    )

    class Meta:
        ordering = ["-created_at"]
        verbose_name = "Заявка"
        verbose_name_plural = "Заявки"

    def __str__(self):
        return f"Заявка #{self.pk} ({self.get_status_display()})"
