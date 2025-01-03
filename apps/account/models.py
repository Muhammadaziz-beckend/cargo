from django.db import models
from django.contrib.auth.models import AbstractUser
from django_resized import ResizedImageField
from phonenumber_field.modelfields import PhoneNumberField
from django.utils.translation import gettext_lazy as _

from utils.models import TimeDateAbstract
from utils.validaters import validate_latin_characters
from .meager import UserNewManager


class User(TimeDateAbstract, AbstractUser):
    # CLIENT = "client"
    # SALESMAN = "salesman"
    # ADMIN = "admin"

    # ROLE = (
    #     (ADMIN, _("Админ")),
    #     (CLIENT, _("Покупатель")),
    #     (SALESMAN, _("Продавец")),
    # )

    username = None
    phone = PhoneNumberField(
        _("номер телефона"),
        unique=True,
    )
    first_name = models.CharField(
        _("first name"),
        validators=[validate_latin_characters],
        max_length=150,
        null=True,
    )
    last_name = models.CharField(
        _("last name"),
        validators=[validate_latin_characters],
        max_length=150,
        null=True,
    )
    email = models.EmailField(
        _("email address"),
        blank=True,
        null=True,
    )
    store = models.ForeignKey(
        "cargo.Store",
        models.SET_NULL,
        verbose_name="склад",
        related_name="users",
        blank=True,
        null=True,
    )

    USERNAME_FIELD = "phone"
    REQUIRED_FIELDS = []

    objects = UserNewManager()

    @property
    def get_full_name(self):
        return f"{self.last_name} {self.first_name}"

    get_full_name.fget.short_description = _("полное имя")

    class Meta:
        verbose_name = "пользователь"
        verbose_name_plural = "пользователи"
        ordering = ("-date_joined",)

    def __str__(self):
        return f"{self.get_full_name or str(self.phone)}"
    
    def get_current_warehouse(self):
        # Возвращает текущий склад
        return self.warehouse
