from django.db import models

from utils.models import TimeDateAbstract
from utils.validaters import MinLengthValidator


class Trek(TimeDateAbstract):
    number_trek = models.IntegerField(
        "трек-код",
        validators=[MinLengthValidator(5)],
    )
    description = models.TextField(
        "Описание",
    )
    owner = models.ForeignKey(
        "account.User",  # Указываем строкой
        models.CASCADE,
        verbose_name="user",
        related_name="treks",
        blank=True,
        null=True,
    )
    china = models.DateTimeField(
        "Прибытия в Китай",
        null=True,
        blank=True,
    )
    store = models.DateTimeField(
        "Прибытия в склада",
        null=True,
        blank=True,
    )
    client = models.DateTimeField(
        "Прибытия к клиенту",
        null=True,
        blank=True,
    )
    store_user = models.ForeignKey(
        "Store",
        models.CASCADE,
        related_name="traces",
        verbose_name="Склад",
        null=True,
        blank=True,
    )
    is_archived = models.BooleanField(
        "Архив",
        default=False,
    )

    def __str__(self):
        return f"{self.number_trek} "
                            # {self.owner}
        

    class Meta:
        verbose_name = "трек"
        verbose_name_plural = "треки"


class Store(TimeDateAbstract):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "склад"
        verbose_name_plural = "склады"
