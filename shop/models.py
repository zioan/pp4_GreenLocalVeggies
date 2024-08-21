from django.db import models
from django.core.validators import MinValueValidator
from decimal import Decimal


class Product(models.Model):
    """
    Represents a product in the shop, including details such as name,
    description, price, stock quantity, unit of measurement, category,
    and an associated image.
    """

    CATEGORY_CHOICES = [
        ("Fruit", "Fruit"),
        ("Vegetable", "Vegetable"),
    ]

    UNIT_CHOICES = [
        ("kg", "kg"),
        ("piece", "piece"),
    ]

    name = models.CharField(max_length=100)
    description = models.TextField()
    price = models.DecimalField(
        max_digits=10,
        decimal_places=2,
        validators=[MinValueValidator(Decimal('0.01'))]
    )
    stock = models.PositiveIntegerField(validators=[MinValueValidator(0)])
    unit = models.CharField(max_length=10, choices=UNIT_CHOICES)
    category = models.CharField(max_length=20, choices=CATEGORY_CHOICES)
    image = models.ImageField(upload_to="products/")
    slug = models.SlugField(unique=True)

    def reduce_stock(self, quantity):
        if self.stock >= quantity:
            self.stock -= quantity
            self.save()
            return True
        return False

    def __str__(self):
        """
        Returns the string representation of the product, which is its name.
        """
        return self.name

    class Meta:
        ordering = ['name']
