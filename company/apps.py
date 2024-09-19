"""Module providing app configuration."""

from django.apps import AppConfig


class CompanyConfig(AppConfig):
    """Company app configuration"""
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'company'
