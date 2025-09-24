from rest_framework import serializers
from products.models import Product
from .models import WishlistItem

class ProductMiniSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = ["id", "name", "price"]

class WishlistItemSerializer(serializers.ModelSerializer):
    product = ProductMiniSerializer(read_only=True)

    class Meta:
        model = WishlistItem
        fields = ["id", "product", "created_at"]

class WishlistAddSerializer(serializers.Serializer):
    product_id = serializers.IntegerField()

    def validate_product_id(self, value):
        try:
            product = Product.objects.get(pk=value)
        except Product.DoesNotExist:
            raise serializers.ValidationError("Product not found.")
        return value

    def save(self, **kwargs):
        user = self.context["request"].user
        product = Product.objects.get(pk=self.validated_data["product_id"])
        item, _created = WishlistItem.objects.get_or_create(user=user, product=product)
        return item
