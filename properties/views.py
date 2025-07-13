#!/usr/bin/env python3
"""Property views with caching"""

from django.http import JsonResponse
from django.views.decorators.cache import cache_page
from .utils import get_all_properties

@cache_page(60 * 15)  # Cache the entire view response for 15 minutes
def property_list(request):
    """Return all properties using low-level caching"""
    properties_qs = get_all_properties()
    properties = list(properties_qs.values())  # Serialize queryset
    return JsonResponse({"data": properties}, safe=False)
