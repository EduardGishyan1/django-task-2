from rest_framework import serializers
from .models import ChildProfile

class ChildProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = ChildProfile
        fields = ["id", "name", "birth_date", "gender"]
        read_only_fields = ["id"]
