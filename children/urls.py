# urls.py
from django.urls import path
from .views import (
    ChildProfileListCreateView,
    ChildProfileDetailView,
    ChildrenListPageView,
    ChildrenAddPageView,
    ChildrenSelectPageView,
)

urlpatterns = [
    path("/list-page",  ChildrenListPageView.as_view(),   name="children-list-page"),
    path("/add-page",   ChildrenAddPageView.as_view(),    name="children-add-page"),
    path("/select-page", ChildrenSelectPageView.as_view(), name="children-select-page"),

    path("/<int:pk>/",   ChildProfileDetailView.as_view(), name="child-detail"),
    path("",           ChildProfileListCreateView.as_view(), name="children-list-create"),
]
