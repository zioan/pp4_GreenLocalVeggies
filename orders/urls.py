from django.urls import path
from . import views

urlpatterns = [
    path('checkout/', views.checkout, name='checkout'),
    path('order-history/', views.order_list, name='order-history'),
    path('<int:order_id>/', views.order_detail, name='order-detail'),
    path('payment-success/', views.payment_success, name='payment_success'),
    path('cancel/<int:order_id>/', views.cancel_order, name='cancel-order'),
]
