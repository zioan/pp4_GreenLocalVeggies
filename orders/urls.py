from django.urls import path
from . import views

urlpatterns = [
    path('checkout/', views.checkout, name='checkout'),
    path('order-history/', views.order_list, name='order-history'),
    path('<int:order_id>/', views.order_detail, name='order-detail'),
]
