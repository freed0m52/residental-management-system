from django.db import models
from django.urls import reverse
from django.utils.text import slugify
from django.db.models import Case, When, Value


class Premise(models.Model):
    """Модель помещения."""
    number = models.PositiveIntegerField(verbose_name="Номер помещения")
    premise_type = models.CharField(max_length=50, verbose_name="Тип")
    area = models.FloatField(verbose_name="Площадь")

    slug = models.SlugField(
        max_length=180,
        unique=True,
        blank=True,
        editable=False,
        verbose_name="URL-идентификатор"
    )

    is_large = models.GeneratedField(
        expression=Case(
            When(area__gte=100.0, then=Value(True)),
            default=Value(False),
            output_field=models.BooleanField(),
        ),
        output_field=models.BooleanField(),
        db_persist=True,
        verbose_name="Большое помещение (от 100 кв.м)"
    )

    class Meta:
        ordering = ["number"]
        verbose_name = "Помещение"
        verbose_name_plural = "Помещения"

    def __str__(self):
        return f"Помещение №{self.number}"

    def save(self, *args, **kwargs):
        if not self.slug:
            transliterated = f"premise-{self.number}"
            base_slug = slugify(transliterated) or "room"
            if self.pk:
                self.slug = f"{base_slug}-{self.pk}"
            else:
                super().save(*args, **kwargs)
                self.slug = f"{base_slug}-{self.pk}"
                super().save(update_fields=["slug"])
                return
        super().save(*args, **kwargs)

    def get_absolute_url(self):
        """Возвращает URL страницы помещения."""
        return reverse("premises:detail", kwargs={"slug": self.slug})
