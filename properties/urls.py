#!/usr/bin/env python3
"""URL config for properties app"""

from django.urls import path
from . import views

urlpatterns = [
    path('', views.property_list, name='property_list'),
]
