# moderators/apps.py
from django.apps import AppConfig

class ModeratorsConfig(AppConfig):
    name = 'moderators'

    def ready(self):
        # Правильный импорт модуля signals
        from . import signals