from django.apps import AppConfig


class CustomuserConfig(AppConfig):
    name = 'CustomUser'

    def ready(self):
        from . import signals
        return super().ready()