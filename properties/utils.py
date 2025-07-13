#!/usr/bin/env python3
"""Utility functions for caching Property queryset"""

from django.core.cache import cache
from .models import Property
import logging

logger = logging.getLogger(__name__)

def get_all_properties():
    """
    Get all Property objects from cache or database.

    Checks Redis for 'all_properties'. If not found, fetches
    from DB and stores queryset in Redis for 1 hour (3600 seconds).
    """
    properties = cache.get('all_properties')
    if properties is None:
        properties = Property.objects.all()
        cache.set('all_properties', properties, timeout=3600)  # Cache for 1 hour
    return properties

def get_redis_cache_metrics():
    """
    Retrieve Redis cache hit/miss metrics and calculate hit ratio.

    Returns:
        dict: {
            'hits': int,
            'misses': int,
            'hit_ratio': float
        }
    """
    # Access the underlying Redis client
    client = cache.master_client
    info = client.info()  # Get all server stats

    hits = info.get('keyspace_hits', 0)
    misses = info.get('keyspace_misses', 0)

    total = hits + misses
    hit_ratio = (hits / total) if total > 0 else 0.0

    metrics = {
        'hits': hits,
        'misses': misses,
        'hit_ratio': round(hit_ratio, 2)  # Rounded to 2 decimal places
    }

    logger.info(f"Redis Cache Metrics: {metrics}")

    return metrics
