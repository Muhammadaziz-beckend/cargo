from django.db import models
from django.core.validators import MinValueValidator

from utils.validaters import MinLengthValidator
from utils.models import TimeDateAbstract

class Warehouse(TimeDateAbstract):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "склад"
        verbose_name_plural = "склады"


class Trek(TimeDateAbstract):
    CHINA = "China"
    CLIENT = "Client"
    
    # Изначальное значение для store
    store = "None"

    # Состояния для выбора статуса
    STATUS_CHOICE = (
        (CHINA, "Китай"),
        (CLIENT, "Клиент"),
        (store, store),  # Это значение будет изменяться динамически
    )

    number_trek = models.IntegerField(
        "трек-код",
        validators=[MinLengthValidator(5)],
    )
    description = models.TextField("Описание")
    owner = models.ForeignKey(
        "account.User",
        models.CASCADE,
        related_name="treks",
    )
    status = models.CharField(
        "статус",
        max_length=6,
        choices=STATUS_CHOICE,
        blank=True,
        null=True,
    )
    warehouse = models.ForeignKey(
        "Warehouse",
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name="treks",
    )

    def __str__(self):
        return f"{self.number_trek} {self.owner}"

    # Метод для обновления status и store
    def update_status_and_store(self):
        if self.warehouse:
            self.store = self.warehouse.name  # Обновляем store с названием склада
            self.status = self.store  # Статус будет равен названию склада

        # Если склада нет, устанавливаем статус как "Клиент" по умолчанию
        elif not self.warehouse and not self.status:
            self.status = self.CLIENT

        # Обновляем выбор для status
        self._meta.get_field('status').choices = self.get_status_choices()

    def get_status_choices(self):
        # Возвращаем обновленный выбор для поля status
        return (
            (self.CHINA, "Китай"),
            (self.store, self.store),
            (self.CLIENT, "Клиент"),
        )

    def save(self, *args, **kwargs):
        # Обновляем статус перед сохранением
        self.update_status_and_store()
        super().save(*args, **kwargs)

    class Meta:
        verbose_name = "трек"
        verbose_name_plural = "треки"
