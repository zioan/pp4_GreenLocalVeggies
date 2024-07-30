from django.db import models
from django.core.validators import MinValueValidator
from decimal import Decimal

# Create your models here.


class Product(models.Model):
    CATEGORY_CHOICES = [
        ("Fruit", "Fruit"),
        ("Vegetable", "Vegetable"),
    ]

    UNIT_CHOICES = [
        ("Kg", "Kg"),
        ("g", "g"),
        ("unit", "unit"),
    ]

    name = models.CharField(max_length=100)
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2, validators=[MinValueValidator(Decimal('0.01'))])
    stock = models.DecimalField(max_digits=10, decimal_places=2, validators=[MinValueValidator(Decimal('0'))])
    unit = models.CharField(max_length=10, choices=UNIT_CHOICES)
    category = models.CharField(max_length=20, choices=CATEGORY_CHOICES)
    image = models.ImageField(upload_to="products/")
    slug = models.SlugField(unique=True)
    allow_half_units = models.BooleanField(
        default=False, help_text="Allow half units for this product")

    def __str__(self):
        return self.name
