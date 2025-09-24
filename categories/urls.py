from django.urls import path
from .views import CategoryListCreateView, CategoryPageView

urlpatterns = [
    path("", CategoryListCreateView.as_view(), name="category-create"),
    path("/page", CategoryPageView.as_view(), name="category-page"),
]