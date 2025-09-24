from rest_framework import generics, permissions
from django.views.generic import TemplateView
from .models import ChildProfile
from .serializers import ChildProfileSerializer

class ChildProfileListCreateView(generics.ListCreateAPIView):
    serializer_class = ChildProfileSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        qs = ChildProfile.objects.filter(parent=self.request.user).order_by("-id")
        q = self.request.query_params.get("q")
        if q:
            qs = qs.filter(name__icontains=q)
        return qs

    def perform_create(self, serializer):
        serializer.save(parent=self.request.user)

class ChildProfileDetailView(generics.RetrieveAPIView):
    serializer_class = ChildProfileSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        return ChildProfile.objects.filter(parent=self.request.user)

class ChildrenListPageView(TemplateView):
    template_name = "children_list.html"

class ChildrenAddPageView(TemplateView):
    template_name = "children_add.html"

class ChildrenSelectPageView(TemplateView):
    template_name = "children_select.html"
