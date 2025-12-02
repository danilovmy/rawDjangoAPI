"""
URL configuration for api project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/dev/topics/http/urls/
Examples:
"""

from django.urls import path, include
from .views import PetListView, PetDetailView

app_name = "api"


urlpatterns = [
    path('pets/', PetListView.as_view(), name='pet-list'),
    path('pets/<int:pk>/', PetDetailView.as_view(), name='pet-detail'),
]
