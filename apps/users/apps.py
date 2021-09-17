"""User aplication module"""
from django.apps import AppConfig


class UsersConfig(AppConfig):
    """User aplication settings"""
    default_auto_field = 'django.db.models.BigAutoField'
    
    verbose_name = 'Users'
    name = 'apps.users'