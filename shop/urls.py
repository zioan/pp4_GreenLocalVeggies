from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path('<slug:product_slug>',
         views.product_details, name="product-details"),
    path('add-to-cart/<int:product_id>/',
         views.add_to_cart, name='add_to_cart'),
    path('about/', views.about, name='about'),
    path('contact/', views.contact, name='contact'),
]
