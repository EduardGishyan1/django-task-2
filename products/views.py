from django.views.generic import TemplateView
from rest_framework import generics, permissions
from django.db.models import Q
from .models import Product
from .serializers import ProductSerializer

class ProductListCreateView(generics.ListCreateAPIView):
    serializer_class = ProductSerializer
    permission_classes = [permissions.AllowAny]
    authentication_classes = []

    def get_queryset(self):
        qs = Product.objects.select_related("category").all()
        q = self.request.query_params.get("q")
        category_id = self.request.query_params.get("category_id")
        if q:
            qs = qs.filter(Q(name__icontains=q.strip()))
        if category_id:
            qs = qs.filter(category_id=category_id)
        return qs

class ProductAddPageView(TemplateView):
    template_name = "product_create.html"

class ProductListPageView(TemplateView):
    template_name = "product_list.html"
