#!/usr/bin/env python3
"""Property views with caching"""

from django.shortcuts import render
from django.http import JsonResponse
from django.views.decorators.cache import cache_page

from .utils import get_all_properties

@cache_page(60 * 15)  # Cache for 15 minutes
def property_list(request):
    """Return a list of all properties (cached)"""
    properties = get_all_properties()
    return JsonResponse({"data": properties}, safe=False)
