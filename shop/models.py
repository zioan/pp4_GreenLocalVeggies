from django.db import models

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
    price = models.DecimalField(max_digits=10, decimal_places=2)
    stock = models.DecimalField(max_digits=10, decimal_places=2)
    unit = models.CharField(max_length=10, choices=UNIT_CHOICES)
    category = models.CharField(max_length=20, choices=CATEGORY_CHOICES)
    image = models.ImageField(upload_to="products/")

    def __str__(self):
        return self.name
