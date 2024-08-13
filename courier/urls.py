from django.urls import path
from . import views

urlpatterns = [
    path('dashboard/', views.courier_dashboard, name='courier_dashboard'),
    path('order/<int:order_id>/', views.order_detail,
         name='courier_order_detail'),
    path('order/<int:order_id>/deliver/',
         views.mark_delivered, name='courier_mark_delivered'),
]
