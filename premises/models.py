from django.db import models


class Premise(models.Model):
    """Модель помещения."""
    number = models.PositiveIntegerField(verbose_name="Номер помещения")
    premise_type = models.CharField(max_length=50, verbose_name="Тип")
    area = models.FloatField(verbose_name="Площадь")
    is_occupied = models.BooleanField(default=False, verbose_name="Занято")

    class Meta:
        ordering = ["number"]  # Сортировка по умолчанию
        verbose_name = "Помещение"
        verbose_name_plural = "Помещения"

    def __str__(self):
        return f"Помещение №{self.number}"
