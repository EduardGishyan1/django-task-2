from django.views.generic import TemplateView
from rest_framework import generics, permissions
from .models import Category
from .serializers import CategorySerializer

class CategoryListCreateView(generics.ListCreateAPIView):
    queryset = Category.objects.all().order_by("name")
    serializer_class = CategorySerializer
    permission_classes = [permissions.AllowAny]
    authentication_classes = []

class CategoryPageView(TemplateView):
    template_name = "category_create.html"
