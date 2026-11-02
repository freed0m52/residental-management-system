from django.db import models


class Resident(models.Model):
    """Модель жителя."""
    full_name = models.CharField(max_length=200, verbose_name="ФИО")
    apartment_number = models.PositiveIntegerField(verbose_name="Квартира")
    phone = models.CharField(max_length=20, verbose_name="Телефон", blank=True, null=True)
    status = models.CharField(max_length=50, verbose_name="Статус")

    class Meta:
        ordering = ["full_name"]  # Сортировка по умолчанию
        verbose_name = "Житель"
        verbose_name_plural = "Жители"

    def __str__(self):
        return f"{self.full_name} (кв. {self.apartment_number})"
