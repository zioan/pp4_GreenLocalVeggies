from django.urls import path
from . import views

app_name = 'staff_dashboard'

urlpatterns = [
    path('', views.order_list, name='order_list'),
    path('order/<int:order_id>/', views.order_detail, name='order_detail'),
    path('order/<int:order_id>/update-status/',
         views.update_order_status, name='update_order_status'),
]
