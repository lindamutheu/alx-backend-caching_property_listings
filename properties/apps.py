#!/usr/bin/env python3
"""AppConfig for properties app"""

from django.apps import AppConfig

class PropertiesConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'properties'

    def ready(self):
        """Import signals to connect them to model events"""
        import properties.signals
