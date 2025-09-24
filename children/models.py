from django.db import models
from django.contrib import admin
from django.contrib.auth.models import User
from .constants import GENDER_CHOICES

class ChildProfile(models.Model):
    name = models.CharField(max_length=100)
    birth_date = models.DateField()
    parent = models.ForeignKey(User, on_delete=models.CASCADE, related_name="children")
    gender = models.CharField(
        max_length=10,
        choices=GENDER_CHOICES
    )

    class Meta:
        verbose_name = "Child Profile"
        verbose_name_plural = "Kids" 

    def __str__(self):
        return f"{self.name} ({self.parent.username})"
