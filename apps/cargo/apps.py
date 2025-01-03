from django.apps import AppConfig


class CargoConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'apps.cargo'
    verbose_name = "Карго"

    def ready(self):
        from . import signals