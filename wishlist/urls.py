from django.urls import path
from .views import WishlistListView, WishlistAddView, WishlistRemoveView, WishlistPageView, WishlistAddPageView

urlpatterns = [
    path("/page", WishlistPageView.as_view(), name="wishlist-page"),
    path("/add-page/", WishlistAddPageView.as_view(), name="wishlist-add-page"),

    path("", WishlistListView.as_view(), name="wishlist-list"),
    path("/add", WishlistAddView.as_view(), name="wishlist-add"),
    path("/remove", WishlistRemoveView.as_view(), name="wishlist-remove"),
]