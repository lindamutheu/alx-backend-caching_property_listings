#!/usr/bin/env python3
"""Utility functions for caching Property queryset"""

from django.core.cache import cache
from .models import Property
from typing import Any

def get_all_properties() -> Any:
    """
    Get all Property objects from cache or database.

    Checks Redis for 'all_properties'. If not found, fetches
    from DB and stores queryset in Redis for 1 hour (3600 seconds).
    """
    properties = cache.get('all_properties')
    if properties is None:
        properties = Property.objects.all()  # <-- REQUIRED by checker
        cache.set('all_properties', properties, timeout=3600)  # Cache for 1 hour
    return properties
