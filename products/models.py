from django.db import models
from categories.models import Category

class Product(models.Model):
    name = models.CharField(max_length=150)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    category = models.ForeignKey(
        Category,
        on_delete=models.SET_NULL,
        null=True, blank=True,
        related_name="products",
    )

    class Meta:
        ordering = ["name"]

    def __str__(self):
        return self.name
