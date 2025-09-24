from rest_framework import permissions, generics, status
from rest_framework.views import APIView
from rest_framework.response import Response
from django.db.models import Prefetch
from .models import WishlistItem
from .serializers import WishlistItemSerializer, WishlistAddSerializer
from django.views.generic import TemplateView

class WishlistListView(generics.ListAPIView):
    """
    GET /wishlist/  → list current user's wishlist (products included)
    """
    permission_classes = [permissions.IsAuthenticated]
    serializer_class = WishlistItemSerializer

    def get_queryset(self):
        return (
            WishlistItem.objects
            .filter(user=self.request.user)
            .select_related("product")
        )

class WishlistAddView(APIView):
    """
    POST /wishlist/add/ { "product_id": <int> }
    → add (idempotent) and return the wishlist item
    """
    permission_classes = [permissions.IsAuthenticated]

    def post(self, request):
        s = WishlistAddSerializer(data=request.data, context={"request": request})
        s.is_valid(raise_exception=True)
        item = s.save()
        return Response(WishlistItemSerializer(item).data, status=status.HTTP_201_CREATED)

class WishlistRemoveView(APIView):
    """
    DELETE /wishlist/remove/?product_id=<int>
    or DELETE body: { "product_id": <int> }
    → remove if exists (idempotent), return 204
    """
    permission_classes = [permissions.IsAuthenticated]

    def delete(self, request):
        product_id = request.query_params.get("product_id") or request.data.get("product_id")
        if not product_id:
            return Response({"detail": "product_id is required."}, status=status.HTTP_400_BAD_REQUEST)

        (
            WishlistItem.objects
            .filter(user=request.user, product_id=product_id)
            .delete()
        )
        return Response(status=status.HTTP_204_NO_CONTENT)

class WishlistPageView(TemplateView):
    template_name = "wishlist_list.html"

class WishlistAddPageView(TemplateView):
    template_name = "wishlist_add.html"