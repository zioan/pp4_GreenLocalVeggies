# Generated by Django 5.0.6 on 2024-07-19 16:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='unit',
            field=models.CharField(choices=[('Kg', 'Kg'), ('g', 'g'), ('unit', 'unit')], default='l', max_length=10),
            preserve_default=False,
        ),
    ]
