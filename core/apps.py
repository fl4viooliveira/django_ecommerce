from django.apps import AppConfig


class CoreConfig(AppConfig):
    name: str = 'core'

    def ready(self):
        # noinspection PyUnresolvedReferences
        from . import signals

        super().ready()
