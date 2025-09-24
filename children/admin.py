from django.contrib import admin
from .models import ChildProfile

@admin.register(ChildProfile)
class ChildProfileAdmin(admin.ModelAdmin):
    list_display = ("name", "birth_date", "gender", "parent")
    search_fields = ("name", "parent__username")
    list_filter = ("gender",)
