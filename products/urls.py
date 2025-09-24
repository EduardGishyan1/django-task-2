from django.urls import path
from .views import ProductListCreateView, ProductAddPageView, ProductListPageView

urlpatterns = [
    path("/add-page",  ProductAddPageView.as_view(),  name="product-add-page"),
    path("/list-page", ProductListPageView.as_view(), name="product-list-page"),
    path("", ProductListCreateView.as_view(), name="product-list-create"),
]
