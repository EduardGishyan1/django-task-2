from django.conf import settings
from django.db import models
from products.models import Product

class WishlistItem(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name="wishlist_items")
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name="wishlisted_by")
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        constraints = [
            models.UniqueConstraint(fields=["user", "product"], name="uniq_user_product_wishlist")
        ]
        ordering = ["-created_at"]

    def __str__(self):
        return f"{self.user} → {self.product}"
