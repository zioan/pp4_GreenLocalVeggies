# Generated by Django 5.0.6 on 2024-07-31 10:08

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0002_alter_product_price_alter_product_stock'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='product',
            name='allow_half_units',
        ),
        migrations.AlterField(
            model_name='product',
            name='stock',
            field=models.PositiveIntegerField(validators=[django.core.validators.MinValueValidator(0)]),
        ),
        migrations.AlterField(
            model_name='product',
            name='unit',
            field=models.CharField(choices=[('kg', 'kg'), ('piece', 'piece')], max_length=10),
        ),
    ]
