from rest_framework import serializers
from .models import Product
from categories.models import Category

class CategoryNestedSerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ["id", "name"]

class ProductSerializer(serializers.ModelSerializer):
    category_id = serializers.PrimaryKeyRelatedField(
        queryset=Category.objects.all(),
        write_only=True,
        required=False,
        allow_null=True,
    )
    category = CategoryNestedSerializer(read_only=True)

    class Meta:
        model = Product
        fields = ["id", "name", "price", "category_id", "category"]
        read_only_fields = ["id"]

    def create(self, validated_data):
        category = validated_data.pop("category_id", None)
        product = Product.objects.create(**validated_data, category=category)
        return product

    def update(self, instance, validated_data):
        category = validated_data.pop("category_id", None)
        for k, v in validated_data.items():
            setattr(instance, k, v)
        if category is not None:
            instance.category = category
        instance.save()
        return instance
