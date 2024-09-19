"""Module providing ORM Models"""
from django.db import models


class Employee(models.Model):
    """Employee model class"""
    full_name = models.CharField(max_length=255)
    position = models.CharField(max_length=100)
    phone_number = models.CharField(max_length=100, blank=True, null=True)
    birth_date = models.DateField(null=True, blank=True)
    email = models.EmailField(null=True, blank=True)
    department = models.ForeignKey(
        'company.Department',
        on_delete=models.CASCADE,
        related_name='employees',
        null=True
    )


class Department(models.Model):
    """Department model class"""
    name = models.CharField(max_length=255)
    store = models.IntegerField(unique=True)
    branch = models.ForeignKey(
        'company.Branch',
        on_delete=models.SET_NULL,
        related_name='departments',
        null=True
    )


class Branch(models.Model):
    """Branch model class"""
    address = models.CharField(max_length=255, blank=True, null=True)
    short_name = models.CharField(max_length=100)
